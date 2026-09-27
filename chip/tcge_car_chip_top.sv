// TCGE Car Chip v0.1
// Safety-compute demonstrator only.
// Not qualified for automotive deployment.
// No actuator-control outputs are provided.

module tcge_car_chip_top #(
    parameter int WIDTH = 32,
    parameter int WATCHDOG_LIMIT = 1024
) (
    input  logic                 clk,
    input  logic                 rst_n,
    input  logic                 in_valid,
    input  logic [WIDTH-1:0]     in_data,

    output logic                 out_valid,
    output logic [WIDTH-1:0]     out_data,

    output logic                 fault_latched,
    output logic                 mismatch_fault,
    output logic                 watchdog_fault
);

    logic a_valid, b_valid;
    logic [WIDTH-1:0] a_data, b_data;

    logic [$clog2(WATCHDOG_LIMIT+1)-1:0] watchdog_count;

    branching_tee_core #(
        .WIDTH(WIDTH),
        .LEVELS(7)
    ) core_a (
        .clk(clk),
        .rst_n(rst_n),
        .in_valid(in_valid),
        .in_data(in_data),
        .out_valid(a_valid),
        .out_data(a_data)
    );

    branching_tee_core #(
        .WIDTH(WIDTH),
        .LEVELS(7)
    ) core_b (
        .clk(clk),
        .rst_n(rst_n),
        .in_valid(in_valid),
        .in_data(in_data),
        .out_valid(b_valid),
        .out_data(b_data)
    );

    always_comb begin
        mismatch_fault =
            (a_valid != b_valid) ||
            (a_valid && b_valid && (a_data != b_data));
    end

    always_ff @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            watchdog_count <= '0;
            watchdog_fault <= 1'b0;
        end else begin
            if (in_valid) begin
                watchdog_count <= '0;
                watchdog_fault <= 1'b0;
            end else if (watchdog_count < WATCHDOG_LIMIT) begin
                watchdog_count <= watchdog_count + 1'b1;
            end else begin
                watchdog_fault <= 1'b1;
            end
        end
    end

    always_ff @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            fault_latched <= 1'b0;
        end else if (mismatch_fault || watchdog_fault) begin
            fault_latched <= 1'b1;
        end
    end

    // Fail-silent handoff:
    // any latched fault suppresses externally visible result.
    always_comb begin
        if (fault_latched || mismatch_fault || watchdog_fault) begin
            out_valid = 1'b0;
            out_data  = '0;
        end else begin
            out_valid = a_valid && b_valid;
            out_data  = a_data;
        end
    end

endmodule
