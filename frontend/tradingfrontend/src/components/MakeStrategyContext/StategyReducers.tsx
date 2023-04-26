type ActionMap<M extends { [index: string]: any }> = {
    [Key in keyof M]: M[Key] extends undefined
    ? {
        type: Key;
    }
    : {
        type: Key;
        payload: M[Key];
    }
};

export enum Types {
    Create = 'CREATE_PRODUCT',
    Delete = 'DELETE_PRODUCT',
    UpdateStategyCode = 'UPDATE_STRATEGY_CODE',
    CreateBacktest = 'CREATE_BACKTEST',
    DeleteBacktest = 'DELETE_BACKTEST',
    UpdateBacktest = 'UPDATE_BACKTEST',
    AddBacktest = 'ADD_BACKTEST',
    Add = 'ADD_PRODUCT',
    UpdateUser = 'UPDATE_USER',
    UpdateDem = 'UPDATE_DEM',
    UpdateDirs = 'UPDATE_DIRS',
    UpdateLas = 'UPDATE_LAS',
    UpdateModel = 'UPDATE_MODEL',
    UpdateOrtho = 'UPDATE_ORTHO',
    UpdateProcessSettings = 'UPDATE_PROCESS_SETTINGS',
    UpdateTileset = '3D',
    UpdateCRS = 'CRS',
    DeleteAll = 'DELETE_ALL',
}

export enum ServerTypes {
    GetServerTasksFromContext = 'GET_SERVER_TASKS_FROM_CONTEXT',
    PostServerTasks2ContextFromServer = 'POST_SERVER_TASKS_2_CONTEXT_FROM_SERVER',
}

export enum BacktestTypes {
    Update = 'UPDATE_BACKTEST',
}


// Product

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
    strategy_code: StrategyCode;
    strategy_type: string;
    strategy_parameters: string;
    strategy_author: string;
    strategy_status: string;
    strategy_created_date: string;
    strategy_updated_date: string;
}

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
    backtest_description: Description;
    backtest_code: string;
    backtest_type: string;
    backtest_parameters: string;
    backtest_author: string;
    backtest_status: string;
    backtest_html: string;
    backtest_created_date: string;
    backtest_updated_date: string;
  }
  
type StrategyServerTask = {
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

type StrategyServerTaskPayload = {
    [ServerTypes.PostServerTasks2ContextFromServer]: [{
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
        crs: string;
        tileset: boolean;
    }];
}

type SingleBacktestPayload = {
    [Types.CreateBacktest]: {
        backtest_id: string;
        backtest_name: string;
        backtest_description: Description;
        backtest_code: string;
        backtest_type: string;
        backtest_parameters: string;
        backtest_author: string;
        backtest_status: string;
        backtest_html: string;
        backtest_created_date: string;
        backtest_updated_date: string;
    };
    [Types.DeleteBacktest]: {
        backtest_id: string;
    }
    [Types.AddBacktest]: {
        backtest_id: string;
    }
    [Types.UpdateUser]: {
        backtest_id: string;
        backtest_author: string;
    }
    [Types.DeleteAll]: {
        backtest_id: string;
    }
    [BacktestTypes.Update]: {
        backtest_id: string;
        backtest_name: string;
        backtest_description: Description;
        backtest_code: string;
        backtest_type: string;
        backtest_parameters: string;
        backtest_author: string;
        backtest_status: string;
        backtest_html: string;
        backtest_created_date: string;
        backtest_updated_date: string;
    }
}


type StrategyPayload = {
    [Types.Create]: {
        strategy_id: string;
        strategy_name: string;
        strategy_description: string;
        strategy_code: StrategyCode;
        strategy_type: string;
        strategy_parameters: string;
        strategy_author: string;
        strategy_status: string;
        strategy_created_date: string;
        strategy_updated_date: string;
    };
    [Types.UpdateStategyCode]: {
        strategy_id: string;
        strategy_code: StrategyCode;
    }
    [Types.Delete]: {
        strategy_id: string;
    }
    [Types.Add]: {
        strategy_id: string;
    }
    [Types.UpdateUser]: {
        strategy_id: string;
        strategy_author: string;
    }
    [Types.DeleteAll]: {
        strategy_id: string;
    }
}

type StrategyPayloadforRefernce = {
    [Types.Create]: {
        createTime: string;
        uuid: string;
        user: string;
        dirs: string | string[];
        crs: string;
        process_settings: string;
        dem: boolean;
        las: boolean;
        model: boolean;
        ortho: boolean;
        tileset: boolean;
    };
    [Types.Delete]: {
        uuid: string;
    }
    [Types.UpdateUser]: {
        uuid: string;
        user: string;
    }
    [Types.UpdateDem]: {
        uuid: string;
        dem: boolean;
    }
    [Types.UpdateDirs]: {
        uuid: string;
        dirs: string | string[];
    }
    [Types.UpdateLas]: {
        uuid: string;
        las: boolean;
    }
    [Types.UpdateModel]: {
        uuid: string;
        model: boolean;
    }
    [Types.UpdateOrtho]: {
        uuid: string;
        ortho: boolean;
    }
    [Types.UpdateProcessSettings]: {
        uuid: string;
        process_settings: string;
    }
    [Types.UpdateTileset]: {
        uuid: string;
        tileset: boolean;
    }
    [Types.UpdateCRS]: {
        uuid: string;
        crs: string;
    }
    [Types.DeleteAll]: undefined;
}
export type StrategyActions = ActionMap<StrategyPayload>[keyof ActionMap<StrategyPayload>];
export type StrategyServerActions = ActionMap<StrategyServerTaskPayload>[keyof ActionMap<StrategyServerTaskPayload>];
export type SingleBacktestActions = ActionMap<SingleBacktestPayload>[keyof ActionMap<SingleBacktestPayload>];




export const StrategyServerTasksReducer = (state: StrategyServerTask[], action: StrategyServerActions) => {
    switch (action.type) {
        case ServerTypes.PostServerTasks2ContextFromServer:
            return action.payload;
        default:
            return state;
    }
}

export const SingleBacktestReducer = (state: SingleBacktest[], action: SingleBacktestActions) => {
    switch (action.type) {
        case Types.CreateBacktest:
            return [
                ...state,
                {
                    backtest_id: action.payload.backtest_id,
                    backtest_name: action.payload.backtest_name,
                    backtest_description: action.payload.backtest_description,
                    backtest_code: action.payload.backtest_code,
                    backtest_type: action.payload.backtest_type,
                    backtest_parameters: action.payload.backtest_parameters,
                    backtest_author: action.payload.backtest_author,
                    backtest_html: action.payload.backtest_html,
                    backtest_status: action.payload.backtest_status,
                    backtest_created_date: action.payload.backtest_created_date,
                    backtest_updated_date: action.payload.backtest_updated_date,
                }
            ]
        case Types.DeleteBacktest:
            return [
                ...state.filter(task => task.backtest_id !== action.payload.backtest_id)
            ]
        case Types.DeleteAll:
            return []
        case BacktestTypes.Update:
            return [
                ...state.map(task => {
                    if (task.backtest_id === action.payload.backtest_id) {
                        return {
                            backtest_id: action.payload.backtest_id,
                            backtest_name: action.payload.backtest_name,
                            backtest_description: action.payload.backtest_description,
                            backtest_code: action.payload.backtest_code,
                            backtest_type: action.payload.backtest_type,
                            backtest_parameters: action.payload.backtest_parameters,
                            backtest_author: action.payload.backtest_author,
                            backtest_html: action.payload.backtest_html,
                            backtest_status: action.payload.backtest_status,
                            backtest_created_date: action.payload.backtest_created_date,
                            backtest_updated_date: action.payload.backtest_updated_date,
                        }
                    }
                    return task;
                })
            ]
        default:
            return state;
    }
}

export const StrategysReducer = (state: Strategy[], action: StrategyActions) => {
    switch (action.type) {
        case Types.Create:
            return [
                ...state,
                {
                    strategy_id: action.payload.strategy_id,
                    strategy_name: action.payload.strategy_name,
                    strategy_description: action.payload.strategy_description,
                    strategy_code: action.payload.strategy_code,
                    strategy_type: action.payload.strategy_type,
                    strategy_parameters: action.payload.strategy_parameters,
                    strategy_author: action.payload.strategy_author,
                    strategy_status: action.payload.strategy_status,
                    strategy_created_date: action.payload.strategy_created_date,
                    strategy_updated_date: action.payload.strategy_updated_date,
                }
            ]
        case Types.Delete:
            return [
                ...state.filter(task => task.strategy_id !== action.payload.strategy_id),
            ]
        case Types.DeleteAll:
            return []
        case Types.UpdateUser:
            return [
                ...state.map(task => {
                    if (task.strategy_id === action.payload.strategy_id) {
                        return {
                            ...task,
                            strategy_author: action.payload.strategy_author,
                        }
                    }
                    return task;
                })
            ]
        case Types.UpdateStategyCode:
            return [
                ...state.map(task => {
                    if (task.strategy_id === action.payload.strategy_id) {
                        return {
                            ...task,
                            strategy_code: action.payload.strategy_code,
                        }
                    }
                    return task;
                })
            ]

        default:
            return state;
    }
}


export const StrategysReducerForReference = (state: Strategy[], action: StrategyActions | ShoppingCartActions) => {
    switch (action.type) {
        case Types.Create:
            return [
                ...state,
                {
                    createTime: action.payload.createTime,
                    uuid: action.payload.uuid,
                    user: action.payload.user,
                    dem: action.payload.dem,
                    dirs: action.payload.dirs,
                    las: action.payload.las,
                    model: action.payload.model,
                    ortho: action.payload.ortho,
                    process_settings: action.payload.process_settings,
                    crs: action.payload.crs,
                    tileset: action.payload.tileset,
                }
            ]
        case Types.Delete:
            return [
                ...state.filter(task => task.uuid !== action.payload.uuid),
            ]
        case Types.DeleteAll:
            return []
        case Types.UpdateUser:
            return [
                ...state.map(task => {
                    if (task.uuid === action.payload.uuid) {
                        return {
                            ...task,
                            user: action.payload.user,
                        }
                    }
                    return task;
                })
            ]
        case Types.UpdateDem:
            return [
                ...state.map(task => {
                    if (task.uuid === action.payload.uuid) {
                        return {
                            ...task,
                            dem: action.payload.dem,
                        }
                    }
                    return task;
                })
            ]
        case Types.UpdateDirs:
            return [
                ...state.map(task => {
                    if (task.uuid === action.payload.uuid) {
                        return {
                            ...task,
                            dirs: action.payload.dirs,
                        }
                    }
                    return task;
                })
            ]
        case Types.UpdateLas:
            return [
                ...state.map(task => {
                    if (task.uuid === action.payload.uuid) {
                        return {
                            ...task,
                            las: action.payload.las,
                        }
                    }
                    return task;
                })
            ]
        case Types.UpdateModel:
            return [
                ...state.map(task => {
                    if (task.uuid === action.payload.uuid) {
                        return {
                            ...task,
                            model: action.payload.model,
                        }
                    }
                    return task;
                })
            ]
        case Types.UpdateOrtho:
            return [
                ...state.map(task => {
                    if (task.uuid === action.payload.uuid) {
                        return {
                            ...task,
                            ortho: action.payload.ortho,
                        }
                    }
                    return task;
                })
            ]
        case Types.UpdateProcessSettings:
            return [
                ...state.map(task => {
                    if (task.uuid === action.payload.uuid) {
                        return {
                            ...task,
                            process_settings: action.payload.process_settings,
                        }
                    }
                    return task;
                })
            ]
        case Types.UpdateTileset:
            return [
                ...state.map(task => {
                    if (task.uuid === action.payload.uuid) {
                        return {
                            ...task,
                            tileset: action.payload.tileset,
                        }
                    }
                    return task;
                })
            ]
        case Types.UpdateCRS:
            return [
                ...state.map(task => {
                    if (task.uuid === action.payload.uuid) {
                        return {
                            ...task,
                            crs: action.payload.crs,
                        }
                    }
                    return task;
                })
            ]

        default:
            return state;
    }
}

// ShoppingCart

// type ShoppingCartPayload = {
//     [Types.Add]: undefined;
// }

// export type ShoppingCartActions = ActionMap<ShoppingCartPayload>[keyof ActionMap<ShoppingCartPayload>];

// export const shoppingCartReducer = (state: number, action: StrategyActions | ShoppingCartActions) => {
//     switch (action.type) {
//         case Types.Add:
//             return state + 1;
//         default:
//             return state;
//     }
// }