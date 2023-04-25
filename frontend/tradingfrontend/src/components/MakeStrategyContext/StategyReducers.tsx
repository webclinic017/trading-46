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


// Product

type MetashapeTask = {
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

}


type MetashapeServerTask = {
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

type MetashapeServerTaskPayload = {
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



type MetashapeTaskPayload = {
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
export type MetashapeActions = ActionMap<MetashapeTaskPayload>[keyof ActionMap<MetashapeTaskPayload>];
export type MetashapeServerActions = ActionMap<MetashapeServerTaskPayload>[keyof ActionMap<MetashapeServerTaskPayload>];




export const metashapeServerTasksReducer = (state: MetashapeServerTask[], action: MetashapeServerActions) => {
    switch (action.type) {
        case ServerTypes.PostServerTasks2ContextFromServer:
            return action.payload;
        default:
            return state;
        }
    }


export const metashapeTasksReducer = (state: MetashapeTask[], action: MetashapeActions | ShoppingCartActions) => {
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

type ShoppingCartPayload = {
    [Types.Add]: undefined;
}

export type ShoppingCartActions = ActionMap<ShoppingCartPayload>[keyof ActionMap<ShoppingCartPayload>];

export const shoppingCartReducer = (state: number, action: MetashapeActions | ShoppingCartActions) => {
    switch (action.type) {
        case Types.Add:
            return state + 1;
        default:
            return state;
    }
}