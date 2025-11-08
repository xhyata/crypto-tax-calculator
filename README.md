# Crypto Tax Calc 
[![Twitter Follow](https://img.shields.io/twitter/url/https/twitter.com/cloudposse.svg?style=social&label=Follow%20@bartoMer177)](https://x.com/bartoMerl77)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Donate](https://img.shields.io/badge/Donate-PayPal-black.svg)](https://www.paypal.com/donate?business=)

# Introduction
Crypto Tax Calculator is an open-source model with UIE (Unified Import Engine) support for crypto and personal income tax calculation. It is designed for individuals, accountants, and organizations that require transparency, precision, and compliance across multiple tax jurisdictions. CryptoTaxCalc helps users consolidate all crypto activity — trades, transfers, staking, airdrops, mining rewards, NFT sales, and more — into a clear, tax-compliant report.

# Getting Started
**To use Crypto-Tax-Calc, your machine must meet the following requirements:**
1. Windows/MacOS
2. Git
3. At least 4GB of RAM
4. Python 3.10+ (all versions above are supported)
   
**To install the program on your machine, follow these instructions:**
1. Install the program on your machine.
```bash
git clone https://github.com/Uak0/crypto-tax-calculator
```
2. Setup the program.
```bash
cd crypto-tax-calculator
python setup.py
```
This will install all the required packages and prepare the program to work out of the box.

# Configuration
Edit the crypto_tax_calculator.conf file to configure the program. All the parameters used in the configuration are listed below.

| Parameter | Default Value | Description |
|------------|----------------|--------------|
| **base_currency** | `'USD'` | Main fiat currency used for all calculations and final reports. You can change it to `'EUR'`, `'GBP'`, etc. |
| **timezone** | `'Europe/London'` | Local timezone applied to all transaction timestamps. Must be a valid [IANA timezone string](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). |
| **date_is_day_first** | `True` | Defines date format: `True` → DD/MM/YYYY, `False` → MM/DD/YYYY. |
| **fiat_currencies** | `[USD, EUR, GBP, JPY, AUD]` | List of fiat currencies used in your transaction records. Add or remove as needed based on your data. |
| **crypto_currencies** | `[BTC, ETH, USDT, BNB, SOL, XRP, DOGE]` | List of supported cryptoassets. Most major cryptocurrencies are supported — you can freely extend this list. |
| **price_data_sources.fiat** | `[ExchangeRateAPI, ECB]` | APIs used to fetch historical fiat currency exchange rates for conversion. |
| **price_data_sources.crypto** | `[CoinGecko, CryptoCompare]` | APIs used to retrieve historical cryptocurrency prices. Multiple sources improve accuracy and redundancy. |
| **trade_value_method** | `2` | Determines how the trade value is calculated:<br>• `0` – use buy-side value<br>• `1` – use sell-side value<br>• `2` – use priority value *(recommended)* |
| **fee_handling_mode** | `2` | Defines how transaction fees are treated:<br>• `0` – ignore fees<br>• `1` – treat as expense<br>• `2` – include in cost basis *(recommended)* |
| **transfer_fees_taxable** | `True` | If `True`, transfer fees (e.g. blockchain fees) are treated as taxable disposals. |
| **include_transfers** | `False` | Whether to include wallet-to-wallet transfers in tax calculations. Usually disabled to avoid double counting. |
| **lost_tokens_as_loss** | `True` | If enabled, tokens marked as *lost* or *burned* are considered realized capital losses. |
| **show_empty_wallets** | `False` | Whether to display wallets with zero balance in generated reports. |
| **hide_zero_balances** | `True` | Hides assets with a zero total value from the reports for better readability. |
| **optimize_large_data** | `False` | Enables optimization for large transaction datasets. Increases speed at the cost of higher memory usage. |
| **debug_mode** | `False` | Enables verbose logging for debugging and troubleshooting. Recommended only during testing. |

# Usage
You can run Crypto Tax Calc from the command line or use it interactively.
The program automatically detects the exchange source, converts data, fetches historical prices, and calculates taxes.

**Option 1 — Direct File Processing (Recommended)**

If you have an exchange export (e.g. Binance, Kraken, Coinbase), simply run:

```bash
cryptotaxcalc ./data/binance_2024.csv
```

The program will automatically:

- Detect the source exchange
- Convert the file to a unified internal format
- Fetch historical prices
- Calculate capital gains and personal income taxes
- Generate a PDF/CSV report

Output example:
```bash
Report successfully generated: ./reports/tax_report_2024.pdf
```
**Option 2 — Interactive Mode**

You can also start an interactive session without arguments:
```bash
cryptotaxcalc
```
This will open the CLI interface.


# Supported crypto exchanges and wallets:
- [X] [Binance](https://www.binance.com/)
- [X] [Bitmart](https://bitmart.com/)
- [X] [MEXC](https://mexc.com/)
- [X] [BingX](https://bingx.com/invite/0EM9RX)
- [X] [Bybit](https://bybit.com/)
- [X] [Gate.io](https://www.gate.io/ref/6266643)
- [X] [HTX (Huobi)](https://www.htx.com/)
- [X] [Kraken](https://kraken.com/)
- [X] [Bitfinex](https://trading.bitfinex.com/)
- [X] [BitPanda](https://www.bitpanda.com/)
- [X] [CEX.IO](https://cex.io/)
- [X] [KuCoin](https://www.kucoin.com/)
- [X] [OKX](https://okx.com/)
- [X] [Hyperliquid](https://hyperliquid.xyz/)
- [ ] [potentially many others](https://github.com/Uak0/crypto-tax-calc/)

### Blockhain Explorers:
- [X] [Etherscan](https://etherscan.io/)
- [X] [BscScan](https://bscscan.com/)
- [X] [Arbiscan](https://arbiscan.io/)
- [X] [Polygonscan](https://polygonscan.com/)
- [X] [Optimistic Etherscan](https://optimistic.etherscan.io/)
- [X] [SnowTrace](https://snowtrace.io/)
- [X] [TronScan](https://tronscan.org/)
- [X] [Solscan](https://solscan.io/)
- [X] [OKLink](https://www.oklink.com/)
- [X] [Blockchair](https://blockchair.com/)
- [X] [Blockchain.com](https://www.blockchain.com/explorer)
- [ ] [potentially many others](https://github.com/Uak0/crypto-tax-calc/)

### Wallets:
- [X] [Ledger Live](https://www.ledger.com/ledger-live)
- [X] [Trezor Suite](https://trezor.io/)
- [X] [Coinomi](https://www.coinomi.com/) 
- [X] [Electrum](https://electrum.org/)
- [X] [Exodus](https://www.exodus.com/)
- [X] [Yoroi](https://yoroi-wallet.com/)
- [X] [Zelcore](https://zelcore.io/)
- [X] [Nault](https://nault.pro/)
- [X] [Qt Wallets (e.g. Bitcoin Core)](https://bitcoincore.org/)
- [X] [HandCash](https://handcash.io/)
- [X] [Volt](https://volt.io/)
- [X] [Helium Wallet](https://helium.com/wallet)
- [ ] [potentially many others](https://github.com/Uak0/crypto-tax-calc/)


This list is regularly updated.


# Transaction Types📃

CryptoTaxCalc supports a variety of transaction types to ensure every aspect of your crypto activity is accurately tracked and correctly reflected in your tax reports.  
Each type determines how a transaction is treated in your **capital gains** and **income tax** calculations.

Understanding these types is essential for achieving precise, audit-ready results.

### Deposit
**Definition:**  
A *Deposit* represents incoming crypto or fiat transferred to a wallet or exchange you control.  
For example, moving BTC from your cold wallet to your Binance account.

**Tax treatment:**  
- Not a taxable event by itself.  
- However, any **deposit fee** paid may count as a taxable disposal.  
- Used for internal transfer tracking and portfolio balance verification.  

**Example:**  
> You send 0.5 ETH from your MetaMask to your Coinbase account — record as `Withdrawal` (from MetaMask) and `Deposit` (to Coinbase).

---

### Withdrawal
**Definition:**  
A *Withdrawal* records tokens sent out of a wallet you own.  
It pairs with a `Deposit` when transferring between your own accounts.

**Tax treatment:**  
- Non-taxable unless the **fee** represents a disposal of a cryptoasset.  
- Helps the engine automatically match internal transfers and exclude them from gains.

**Example:**  
> You withdraw 100 USDT from Binance to your Ledger.  
This creates a non-taxable internal transfer.

---

### Trade
**Definition:**  
A *Trade* captures any exchange between assets — crypto-to-crypto, crypto-to-fiat, or fiat-to-crypto.

**Tax treatment:**  
- **Crypto-to-crypto** and **crypto-to-fiat** are considered *disposals*.  
- **Fiat-to-crypto** is an *acquisition*.  
- Used to calculate both realized gains and cost basis adjustments.

**Example:**  
> Selling 1 SOL for 150 USDT triggers a capital gain or loss based on the cost of that SOL.

---

### Mining
**Definition:**  
Records tokens earned as mining rewards.  
Treated as **taxable income** when received.

**Tax treatment:**  
- The value of mined tokens at the time of receipt is considered *income*.  
- Subsequent sale of those tokens counts as *capital gains or losses*.

**Example:**  
> You mined 0.01 BTC on Jan 1, worth $400.  
That $400 is income. Selling it later for $450 creates a $50 gain.

---

### Staking
**Definition:**  
Tokens earned from staking or validator operations.

**Tax treatment:**  
- Counted as *income* when received.  
- Later disposal triggers *capital gains*.  
- If ownership is transferred to a platform (e.g. DeFi staking), additional disposal entries may be required.

**Example:**  
> You staked 10 ADA and received 0.2 ADA rewards — taxable as income at market value on that date.

---

### Interest
**Definition:**  
Tokens received as passive yield, interest, or lending rewards.

**Tax treatment:**  
- Treated as *income*.  
- If interest is auto-compounded, each credited portion is taxed individually.  

**Example:**  
> You earned 5 USDT in interest from a lending platform — it’s taxable income upon credit.

---

### Airdrop
**Definition:**  
Tokens received through project distributions or promotional events.

**Tax treatment:**  
- If received *freely* (no conditions), **not income**.  
- If received *for activity* (e.g. signup, referral, or interaction), **taxed as income**.  
- All airdrops establish a cost basis equal to market value at the time of receipt.

**Example:**  
> You received 50 XYZ tokens from an airdrop campaign after completing a task — taxable as income.

---

### Gift-Received
**Definition:**  
Tokens received as a personal gift from another individual.

**Tax treatment:**  
- Not taxed upon receipt.  
- The *donor’s cost basis* is inherited — meaning gains/losses are calculated from their original purchase value.

---

### Gift-Sent
**Definition:**  
Tokens you’ve given to another individual as a gift.

**Tax treatment:**  
- Considered a **disposal** for capital gains purposes.  
- Value is based on market price at the time of the gift.

---

### Charity-Sent
**Definition:**  
Tokens donated to a registered charity or nonprofit organization.

**Tax treatment:**  
- Treated as a **No-Gain / No-Loss** disposal (tax neutral).  
- Still recorded for full transparency in reports and audits.

---

### Lost
**Definition:**  
Used to record tokens that are permanently inaccessible.  

**Tax treatment:**  
- Can be treated as a **capital loss**, if a negligible value claim or equivalent proof is accepted.  
- System assumes a disposal at the declared value (default: zero).

---

### Other Cases ⚙
**Fork**  
When a blockchain forks and you receive a new token, record it as `Airdrop` or `Gift-Received` with zero cost.  

**Dust Removal**  
When an exchange removes unusable small token amounts — record as `Spend` with zero proceeds.  

**Fee Disposal**  
When paying transaction or transfer fees, these are often treated as small taxable disposals depending on jurisdiction.

# How to Assign Transaction Types

There are two ways to assign transaction types in CryptoTaxCalc:

1. **Automatic Detection**  
   The **Unified Import Engine (UIE)** analyzes imported CSV or API data from exchanges and wallets to automatically classify transactions by type.  
   It uses pattern matching, keywords, and context analysis to identify trades, transfers, rewards, and other events.
   
2. **Manual Assignment**  
   For custom or unsupported exchanges, you can manually specify transaction types in your CSV before import.  
   Simply include a `type` column with one of the valid type names (e.g. `Trade`, `Deposit`, `Staking`, `Airdrop`).

   ```csv
   date,asset,quantity,price,type
   2024-01-10,BTC,0.05,42000,Trade
   2024-02-02,ADA,20,0.35,Staking
   2024-03-01,SOL,2,80,Deposit


# Donations & Sponsorship

If you find this project useful, consider supporting future development:
- **BTC**: bc1q8grhtxdw37npcdadm7xa848vquqgurj9ecvpex
- **ERC20**: 0x2d19c72fb8b3a7cdc7fa4970b5c777966f547854

**Thank you!🙏**




