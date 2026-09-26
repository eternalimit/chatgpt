# Crypto Top 90 Connector + Settlement-Stability Map

Date: 2026-09-26
Assignment: code.core.main / FACTS
Status: CONNECTOR MAP

## Stability definition

"Stability" here means the transaction-settlement/finality model of the blockchain or host network. It is NOT a price-stability score, investment rating, wallet balance, or ownership claim.

Connector IDs are adapter families for code.core.main. They do not contain private keys, seed phrases, exchange credentials, or signing authority.

| Rank | Asset | Chain / Host | Connector | Settlement stability |
|---:|---|---|---|---|
| 1 | Bitcoin | Bitcoin | `btc` | PoW; probabilistic settlement |
| 2 | Ethereum | Ethereum | `evm-ethereum` | PoS; crypto-economic checkpoint finality |
| 3 | Tether USDt | Multi-chain | `multi-chain` | Host-chain finality + issuer/peg risk |
| 4 | BNB | BNB Smart Chain | `evm-bnb` | Validator-based PoSA/economic finality |
| 5 | XRP | XRP Ledger | `xrpl` | Federated consensus; deterministic ledger finality |
| 6 | USDC | Multi-chain | `multi-chain` | Host-chain finality + issuer/peg risk |
| 7 | Solana | Solana | `solana` | PoS/BFT-style confirmation and finality |
| 8 | TRON | TRON | `tron` | DPoS/Super Representative finality |
| 9 | Zcash | Zcash | `zcash` | PoW; probabilistic settlement |
| 10 | Hyperliquid | Hyperliquid L1 | `hyperliquid` | BFT-style validator finality |
| 11 | Dogecoin | Dogecoin | `dogecoin` | PoW; probabilistic settlement |
| 12 | Monero | Monero | `monero` | PoW; probabilistic settlement |
| 13 | Chainlink | Multi-chain token | `multi-chain` | Inherits selected host-chain finality |
| 14 | Cardano | Cardano | `cardano` | Ouroboros PoS; probabilistic/economic settlement |
| 15 | UNUS SED LEO | Multi-chain token | `multi-chain` | Inherits selected host-chain finality + issuer risk |
| 16 | Stellar | Stellar | `stellar` | SCP federated consensus; deterministic ledger close |
| 17 | Bitcoin Cash | Bitcoin Cash | `bch` | PoW; probabilistic settlement |
| 18 | NEAR Protocol | NEAR | `near` | PoS/BFT-style finality |
| 19 | Uniswap | Ethereum token | `evm-ethereum` | Inherits Ethereum finality |
| 20 | Litecoin | Litecoin | `litecoin` | PoW; probabilistic settlement |
| 21 | Ethena USDe | Ethereum-centric multi-chain token | `multi-chain` | Host-chain finality + protocol/peg risk |
| 22 | Avalanche | Avalanche C-Chain / Primary Network | `avalanche` | Avalanche/Snowman consensus; rapid finality |
| 23 | Dai | Ethereum-centric multi-chain token | `multi-chain` | Host-chain finality + collateral/peg risk |
| 24 | Canton | Canton Network | `canton` | Native network consensus; connector requires network-specific validation |
| 25 | World Liberty Financial USD | Multi-chain stablecoin | `multi-chain` | Host-chain finality + issuer/peg risk |
| 26 | Sui | Sui | `sui` | BFT-style deterministic transaction finality |
| 27 | Hedera | Hedera | `hedera` | Hashgraph aBFT finality |
| 28 | Gram (prev. Toncoin) | UNRESOLVED from snapshot label | `unresolved` | UNRESOLVED; do not assign chain without source confirmation |
| 29 | Bittensor | Bittensor / Subtensor | `bittensor` | Native validator consensus; economic finality |
| 30 | Shiba Inu | Ethereum token | `evm-ethereum` | Inherits Ethereum finality |
| 31 | Global Dollar | Multi-chain stablecoin | `multi-chain` | Host-chain finality + issuer/peg risk |
| 32 | Cronos | Cronos / Crypto.org ecosystem | `evm-cronos` | Validator-based chain finality |
| 33 | MemeCore | MemeCore | `evm-memecore` | Native EVM-chain validator finality |
| 34 | PayPal USD | Multi-chain stablecoin | `multi-chain` | Host-chain finality + issuer/peg risk |
| 35 | Tether Gold | Ethereum-centric token | `multi-chain` | Host-chain finality + issuer/custody risk |
| 36 | OKB | X Layer / Ethereum ecosystem | `evm-xlayer` | Host/native-chain finality depends on selected network |
| 37 | Ondo | Ethereum token | `evm-ethereum` | Inherits Ethereum finality + protocol/issuer dependencies |
| 38 | Ripple USD | XRP Ledger + Ethereum | `multi-chain` | Host-chain finality + issuer/peg risk |
| 39 | Mantle | Mantle L2 | `evm-mantle` | L2 execution; settlement ultimately anchored to Ethereum |
| 40 | Ethena | Ethereum token | `evm-ethereum` | Inherits Ethereum finality |
| 41 | Aave | Ethereum-centric multi-chain token | `multi-chain` | Inherits selected host-chain finality |
| 42 | Polkadot | Polkadot | `polkadot` | BABE + GRANDPA; deterministic finalized blocks |
| 43 | Aster | Multi-chain application/token | `multi-chain` | UNRESOLVED per-chain; validate selected deployment |
| 44 | PAX Gold | Ethereum token | `evm-ethereum` | Inherits Ethereum finality + custodian risk |
| 45 | Pepe | Ethereum token | `evm-ethereum` | Inherits Ethereum finality |
| 46 | Pump.fun | Solana token | `solana` | Inherits Solana finality |
| 47 | World Liberty Financial | Ethereum token | `evm-ethereum` | Inherits Ethereum finality |
| 48 | Sky | Ethereum token | `evm-ethereum` | Inherits Ethereum finality |
| 49 | Internet Computer | Internet Computer | `icp` | Threshold/BFT-style subnet finality |
| 50 | Worldcoin | World Chain / Ethereum ecosystem | `evm-worldchain` | L2 execution; settlement anchored to Ethereum |
| 51 | Ethereum Classic | Ethereum Classic | `evm-etc` | PoW; probabilistic settlement |
| 52 | USDD | TRON-centric multi-chain stablecoin | `multi-chain` | Host-chain finality + collateral/peg risk |
| 53 | Venice Token | Base token | `evm-base` | L2 execution; settlement anchored to Ethereum |
| 54 | Arbitrum | Arbitrum One | `evm-arbitrum` | Optimistic rollup; Ethereum settlement with challenge-window risk |
| 55 | Morpho | Ethereum/Base token | `multi-chain` | Inherits selected host-chain finality |
| 56 | United Stables | UNRESOLVED / multi-chain stablecoin | `unresolved` | UNRESOLVED; connector and peg mechanism require source validation |
| 57 | Bitget Token | Ethereum / exchange ecosystem | `evm-ethereum` | Host-chain finality + issuer/exchange dependency |
| 58 | Lighter | Ethereum L2 / rollup ecosystem | `evm-lighter` | L2 execution; Ethereum settlement model |
| 59 | GateToken | GateChain | `gatechain` | Native validator-chain finality |
| 60 | Polygon (prev. MATIC) | Polygon PoS | `evm-polygon` | PoS checkpoint/validator finality; Ethereum anchoring |
| 61 | Kaspa | Kaspa | `kaspa` | PoW blockDAG; probabilistic settlement |
| 62 | Quant | Ethereum token | `evm-ethereum` | Inherits Ethereum finality |
| 63 | Algorand | Algorand | `algorand` | Pure PoS; immediate/deterministic block finality |
| 64 | Jupiter | Solana token | `solana` | Inherits Solana finality |
| 65 | KuCoin Token | Ethereum / KCC ecosystem | `multi-chain` | Host-chain finality + exchange dependency |
| 66 | Pi | Pi Network | `pi-network` | Native network consensus; validate mainnet accessibility and state |
| 67 | Render | Solana token | `solana` | Inherits Solana finality |
| 68 | Cosmos | Cosmos Hub | `cosmos` | CometBFT/Tendermint; deterministic finality |
| 69 | JUST | TRON token | `tron` | Inherits TRON finality |
| 70 | PancakeSwap | BNB Chain-centric multi-chain token | `multi-chain` | Inherits selected host-chain finality |
| 71 | Filecoin | Filecoin | `filecoin` | Expected Consensus; probabilistic settlement with protocol finality rules |
| 72 | Injective | Injective | `cosmos-injective` | CometBFT/Tendermint-style deterministic finality |
| 73 | Dash | Dash | `dash` | PoW plus quorum/ChainLocks; stronger lock finality after quorum confirmation |
| 74 | VeChain | VeChainThor | `vechain` | PoA validator finality with protocol finality mechanisms |
| 75 | Aptos | Aptos | `aptos` | AptosBFT; deterministic BFT finality |
| 76 | Stable | UNRESOLVED from snapshot label | `unresolved` | UNRESOLVED; identify exact asset/network first |
| 77 | Aerodrome Finance | Base token | `evm-base` | L2 execution; settlement anchored to Ethereum |
| 78 | ether.fi | Ethereum token | `evm-ethereum` | Inherits Ethereum finality |
| 79 | XDC Network | XDC Network | `evm-xdc` | XDPoS/BFT-style validator finality |
| 80 | Pudgy Penguins | Solana token | `solana` | Inherits Solana finality |
| 81 | Flare | Flare | `evm-flare` | Validator/BFT-style native-chain finality |
| 82 | OFFICIAL TRUMP | Solana token | `solana` | Inherits Solana finality |
| 83 | Raydium | Solana token | `solana` | Inherits Solana finality |
| 84 | Stacks | Stacks / Bitcoin-anchored | `stacks` | Bitcoin-anchored settlement; Stacks-specific finality rules |
| 85 | Nexo | Ethereum token | `evm-ethereum` | Inherits Ethereum finality + issuer/platform dependency |
| 86 | LayerZero | Multi-chain token/protocol | `multi-chain` | Token finality depends on host chain; messaging adds cross-chain validation risk |
| 87 | Curve DAO Token | Ethereum-centric multi-chain token | `multi-chain` | Inherits selected host-chain finality |
| 88 | Pyth Network | Solana / Pyth ecosystem | `solana-pyth` | Token finality depends on host chain; oracle data has separate trust model |
| 89 | Artificial Superintelligence Alliance | Multi-chain / Fetch.ai ecosystem | `multi-chain` | Host-chain/native-chain finality depends on selected network |
| 90 | 币安人生 | UNRESOLVED from snapshot label | `unresolved` | UNRESOLVED; identify exact asset/network first |

## TCGE connector rule

For every asset:

GET -> CONNECTOR -> READ PUBLIC CHAIN STATE -> VERIFY -> ECHO -> K

A connector may read public network state. It does not prove ownership. Ownership/balance requires a specific public address plus on-chain evidence, while signing authority remains outside this facts table.

Rows marked UNRESOLVED remain K=0 for chain assignment until an authoritative source identifies the exact asset/network.

## Stability classes

- PoW / probabilistic: confidence increases with confirmations; no single irreversible-finality event.
- PoS/BFT / deterministic or crypto-economic: the protocol exposes a finalized state or equivalent validator-finality condition.
- L2 / inherited settlement: execution occurs on an L2 while ultimate settlement/security depends on a base chain, commonly Ethereum.
- Host-chain token: token settlement inherits the selected blockchain's finality.
- Stablecoin / backed asset: blockchain settlement can be final while peg, issuer, reserve, collateral, or custody risk remains separate.
- Multi-chain: stability must be evaluated on the exact chain used for a specific transaction.

## Evidence boundary

This map is a connector architecture and settlement-model classification. It does not claim that every connector has been implemented or live-tested. Per-chain production activation requires independent endpoint/schema validation and a read-only test before K=1 can be assigned to the connector itself.
