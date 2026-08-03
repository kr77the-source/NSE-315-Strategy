\# Production F\&O Algorithmic Trading Engine v1.0



Institutional-grade modular intraday trading system built for the Indian F\&O market. Features real-time Open Interest (OI) spurts scanning, sideways elimination via ATR/Range, Inside Bar price action strategy, volume confirmation, multi-table SQLite audit logging, risk controls, and broker API integration.



\## Architecture

\- `main.py`: Core orchestrator \& 5-minute continuous scanning loop.

\- `market.py`: Market timing, holidays, and NSE universe management.

\- `scanner.py`: OI Spurts ranking and range filtering.

\- `strategy.py`: PDH/PDL, Inside Candle, and Volume rules.

\- `risk\_manager.py`: Capital protection, position sizing, and exposure limits.

\- `broker.py`: Multi-broker execution wrapper.

\- `database.py`: 7-table normalized storage system.

