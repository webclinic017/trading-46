import React, { createContext, useReducer, Dispatch } from 'react';
import { StrategyTasksReducer, shoppingCartReducer, StrategyActions, ShoppingCartActions, StrategyServerActions } from './StrategyReducers';
type StrategyTask = {
    createTime: string;
    uuid: string;
    user: string;
    dem: number;
    dirs: string | string[];
    las: boolean;
    model: boolean;
    ortho: boolean;
    process_settings: string;
    crs: string;
    
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
  
  type InitialStateType = {
    StrategyTasks: StrategyTask[];
    // StrategyServerTasks:StrategyServerTask[],
    // shoppingCart: number;
  }
  
  const initialState = {
    StategyTasks: [],
    StrategyServerTasks:[],
    shoppingCart: 0,
  }
  
  const StrategyContext = createContext<{
    state: InitialStateType;
    dispatch: Dispatch<StrategyActions | ShoppingCartActions| StrategyServerActions>;
  }>({
    state: initialState,
    dispatch: () => null
  });
  



export { StrategyContext };