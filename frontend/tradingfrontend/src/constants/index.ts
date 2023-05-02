export const BOARD_SECTIONS = {
  backlog: 'backlog',
  'in progress': 'in progress',
  done: 'done',
};


export const BACKTEST_API_NODE = 'http://localhost:8000/api';
export const BACKTEST_API_VERSION = 'v1';
export const BACKTEST_API_URL = BACKTEST_API_NODE + '/' + BACKTEST_API_VERSION;
export const AUTH_API_NODE = BACKTEST_API_URL + '/auth/';
export const BACKTEST_API = BACKTEST_API_URL + '/backtest/';
export const STRATEGY_API = BACKTEST_API_URL + '/strategies/';



// For production
// export const BACKTEST_API_NODE = 'http://localhost:8050';
