import React, { createContext, useReducer, Dispatch } from 'react';
import { StrategyTasksReducer, shoppingCartReducer,SingleBacktestReducer, StrategyActions, ShoppingCartActions, StrategyServerActions } from './StrategyReducers';
type StrategyCode = {
  init_indicators: string[];
  stop_loss: number;
  take_profit: number;
  buy_first: boolean;
  buy_signal: string[][];
  sell_signal: string[][];
}

type Strategy = {
  strategy_id: string;
  strategy_name: string;
  strategy_description: string;
  strategy_code: [StrategyCode];
  strategy_type: string;
  strategy_parameters: string;
  strategy_author: string;
  strategy_status: string;
  strategy_created_date: string;
  strategy_updated_date: string;
}


type StrategyServerTask = {
  crs: string;
  createTime: string;
  status: string;
  _id: string;
  uuid: string;
  user: string;
  dem: number;
  dirs: string | string[];
  las: boolean;
  model: boolean;
  ortho: boolean;
  process_settings: string;

}


// class Description(EmbeddedModel):
//     stock_symbol: str = Field(...)
//     stock_name: str = Field(...)
//     start_date: str = Field(...)
//     end_date: str = Field(...)
//     strategy_name: str = Field(...)
//     commission: float = Field(...)
//     cash: float = Field(...)

// class SingleBacktest(Model):
//     backtest_id: str = Field(...)
//     backtest_name: str = Field(...)
//     backtest_description: str = Field(...)
//     backtest_code: str = Field(...)
//     backtest_type: str = Field(...)
//     backtest_parameters: str = Field(...)
//     backtest_author: str = Field(...)
//     backtest_status: str = Field(...)
//     backtest_created_date: datetime = Field(default_factory=datetime.now)
//     backtest_updated_date: datetime = Field(default_factory=datetime.now)

type Description = {
  stock_symbol: string;
  stock_name: string;
  start_date: string;
  end_date: string;
  strategy_name: string;
  commission: number;
  cash: number;
}

type SingleBacktest = {
  backtest_id: string;
  backtest_name: string;
  backtest_description: string;
  backtest_code: string;
  backtest_type: string;
  backtest_parameters: string;
  backtest_author: string;
  backtest_status: string;
  backtest_html: string;
  backtest_created_date: string;
  backtest_updated_date: string;
}

type InitialStateType = {
  Strategy: Strategy[];
  Backtest: SingleBacktest[];
  // StrategyServerTasks:StrategyServerTask[],
  // shoppingCart: number;
}

const initialState = {
  StrategyTasks: [],
  Backtest:[],
  // StrategyServerTasks: [],
  // shoppingCart: 0,
}

const StrategyContext = createContext<{
  state: InitialStateType;
  dispatch: Dispatch<StrategyActions | ShoppingCartActions | StrategyServerActions | SingleBacktestReducer>;
}>({
  state: initialState,
  dispatch: () => null
});




export { StrategyContext };