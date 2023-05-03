import * as React from 'react';
import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';
import Button from '@mui/material/Button';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { useRef, useEffect, useState, useContext } from 'react';
import MakeStrategyBoard from 'src/components/MakeStrategyComponents/MakeStrategyBoard';
import { SortableItem } from '../../pages/SortableItemS';
import Container from 'react-bootstrap/Container';
import Stack from '@mui/material/Stack';
import { StrategyContext } from 'src/components/MakeStrategyContext/StrategyContext';
import { STRATEGY_API } from 'src/constants'
import { BacktestTypes, Types } from 'src/components/MakeStrategyContext/StrategyReducers'
import ImageList from '@mui/material/ImageList';
import ImageListItem from '@mui/material/ImageListItem';
import axios from 'axios';
import { v4 as uuidv4 } from 'uuid';

export default function SelectStrategy() {
    const [strategies, setStrategies] = useState([]);
    useEffect(() => {
        let config = {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('accessToken')}`,
                'Accept': 'application/json'
            }
        }
        axios.get(STRATEGY_API + 'get_strategies_by_author', config).then((response) => {
            console.log(response.data);
            setStrategies(response.data);
            // dispatch({ type: 'SET_STRATEGY_TASKS', payload: response.data });
        });
    }, []);
    const { state, dispatch } = React.useContext(StrategyContext);
    const handleAddStrategy = () => {
        let config = {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('accessToken')}`,
                'Accept': 'application/json'
            }
        }
        let data = {
            "strategy_id": "string",
            "strategy_name": "未命名",
            "strategy_description": "strategy_description",
            "strategy_code": {
                "init_indicators": [
                ],
                "stop_loss": 10,
                "take_profit": 20,
                "buy_first": true,
                "buy_signal": [

                ],
                "sell_signal": [

                ]
            },
            "strategy_type": "strategy_type",
            "strategy_parameters": "strategy_parameters",
            "strategy_author": "strategy_author",
            "strategy_status": "strategy_status",
            "strategy_created_date": "2023-05-03T10:27:20.824015",
            "strategy_updated_date": "2023-05-03T10:27:20.824015"
        }
        axios.post(STRATEGY_API + 'add_strategy', data, config)
            .then((response) => {
                console.log(response.data);
            });
        axios.get(STRATEGY_API + 'get_strategies_by_author', config).then((response) => {
            console.log(response.data);
            setStrategies(response.data);
        });
    }
    const handleSelectStrategy = (strategy) => {
        if (state?.SingleBacktest[0] === undefined) {
            dispatch({
                type: BacktestTypes.CREATE_BACKTEST, payload: {
                    backtest_id: uuidv4(),
                    backtest_name: 'Backtest',
                    backtest_strategy: {
                        strategy_id: strategy.id,
                        strategy_name: strategy.strategy_name
                    },
                    backtest_description: 'Backtest',
                    backtest_code: 'Backtest',
                    backtest_type: 'Backtest',
                    backtest_parameters: 'Backtest',
                    backtest_author: 'Backtest',
                    backtest_html: 'Backtest',
                    backtest_status: 'Backtest',
                    backtest_created_date: 'Backtest',
                    backtest_updated_date: 'Backtest',
                }
            });
            dispatch({
                type: Types.Create,
                payload: {
                    strategy_id: strategy.id,
                    strategy_name: strategy.strategy_name,
                    strategy_description: strategy.strategy_description,
                    strategy_code: strategy.strategy_code,
                    strategy_type: strategy.strategy_type,
                    strategy_parameters: strategy.strategy_parameters,
                    strategy_author: strategy.strategy_author,
                    strategy_status: strategy.strategy_status,
                    strategy_created_date: strategy.strategy_created_date,
                    strategy_updated_date: strategy.strategy_updated_date,
                },
            });
        } else {
            dispatch({
                type: BacktestTypes.UPDATE_BACKTEST_STRATEGY, payload: {
                    backtest_id: state?.SingleBacktest[0].backtest_id,
                    backtest_strategy: strategyId,
                }
            });
        }
        console.log(state?.SingleBacktest[0]);
    }

    return (

        <Box>
            {strategies.map((strategy) => (
                <ImageListItem key={strategy.id}>
                    <Button onClick={() => {
                        handleSelectStrategy(strategy);
                    }}>
                        設定 {strategy.strategy_name} 策略
                    </Button>
                </ImageListItem>
            ))}
            <Button onClick={() => {
                handleAddStrategy();
            }}>
                新增策略
            </Button>
        </Box>

    )
}