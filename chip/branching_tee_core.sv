// TCGE Branching Tee Core v0.1
// 7 levels -> 127 total nodes -> 64 leaves
// Synthesizable reference RTL. This is a logical prototype, not fabricated silicon.

module branching_tee_core #(
    parameter int WIDTH  = 32,
    parameter int LEVELS = 7
) (
    input  logic                 clk,
    input  logic                 rst_n,
    input  logic                 in_valid,
    input  logic [WIDTH-1:0]     in_data,
    output logic                 out_valid,
    output logic [WIDTH-1:0]     out_data
);

    localparam int TOTAL_NODES = (1 << LEVELS) - 1;
    localparam int LEAF_COUNT  = (1 << (LEVELS-1));
    localparam int FIRST_LEAF  = LEAF_COUNT - 1;

    logic [WIDTH-1:0] node_data [0:TOTAL_NODES-1];
    logic             node_valid[0:TOTAL_NODES-1];

    integer i;
    integer j;
    logic [WIDTH-1:0] resolved;

    // Root / point
    always_comb begin
        for (i = 0; i < TOTAL_NODES; i = i + 1) begin
            node_data[i]  = '0;
            node_valid[i] = 1'b0;
        end

        node_data[0]  = in_data;
        node_valid[0] = in_valid;

        // Recursive branching tee.
        // Each child receives the parent payload plus a deterministic branch tag.
        for (i = 0; i < FIRST_LEAF; i = i + 1) begin
            node_valid[(2*i)+1] = node_valid[i];
            node_valid[(2*i)+2] = node_valid[i];

            node_data[(2*i)+1] =
                node_data[i] ^ WIDTH'((2*i)+1);

            node_data[(2*i)+2] =
                {node_data[i][WIDTH-2:0], node_data[i][WIDTH-1]}
                ^ WIDTH'((2*i)+2);
        end

        // Resolve all leaf results into one deterministic output.
        resolved = '0;
        for (j = FIRST_LEAF; j < TOTAL_NODES; j = j + 1) begin
            if (node_valid[j])
                resolved = resolved ^ node_data[j];
        end
    end

    // Registered handoff.
    always_ff @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            out_valid <= 1'b0;
            out_data  <= '0;
        end else begin
            out_valid <= in_valid;
            out_data  <= resolved;
        end
    end

endmodule
