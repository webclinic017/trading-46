import * as React from 'react';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select, { SelectChangeEvent } from '@mui/material/Select';
import Typography from '@mui/material/Typography';
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
import { BacktestTypes,StrategyTypes } from 'src/components/MakeStrategyContext/StrategyReducers'
import ImageList from '@mui/material/ImageList';
import ImageListItem from '@mui/material/ImageListItem';
import axios from 'axios';
import { v4 as uuidv4 } from 'uuid';
export default function SelectStrategySelectBar() {
    const [strategies, setStrategies] = useState([]);
    const { state, dispatch } = React.useContext(StrategyContext);

    const [selectedStrategy, setSelectedStrategy] = useState("");

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
    const handleSelectStrategy = (e) => {
        let selected_strategy_name = '';
        strategies.map((strategy) => {
            if (strategy.id === e.target.value) {
                selected_strategy_name = strategy.strategy_name;
                console.log(strategy);
                dispatch({
                    type: StrategyTypes.UPDATE,
                    payload: {
                        strategy_id : strategy.id,
                        strategy_name : strategy.strategy_name,
                        strategy_description : strategy.strategy_description,
                        strategy_code : strategy.strategy_code,
                        strategy_type : strategy.strategy_type,
                        strategy_parameters : strategy.strategy_parameters,
                        strategy_author : strategy.strategy_author,
                        strategy_status : strategy.strategy_status,
                        strategy_created_date : strategy.strategy_created_date,
                        strategy_updated_date : strategy.strategy_updated_date,
                    },
                  });
            }
        });
        setSelectedStrategy(e.target.value)
        if (state?.SingleBacktest[0] === undefined) {
            dispatch({
                type: BacktestTypes.CREATE_BACKTEST, payload: {
                    backtest_id: uuidv4(),
                    backtest_name: 'Backtest',
                    backtest_strategy: {
                        strategy_id: e.target.value,
                        strategy_name: selected_strategy_name,
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
        } else {
            dispatch({
                type: BacktestTypes.UPDATE_BACKTEST_STRATEGY, payload: {
                    backtest_id: state?.SingleBacktest[0].backtest_id,
                    backtest_strategy: {
                        strategy_id: e.target.value,
                        strategy_name: selected_strategy_name,
                    },
                }
            });
        }
        console.log(state?.SingleBacktest[0]);
    }
    return (
        <>
            {/* <Typography variant="body2" >
                    選擇策略 :
                </Typography> */}
            <FormControl sx={{ m: 1, minWidth: 300 }} size="small">
                <InputLabel  shrink id="demo-select-small-label">選擇策略</InputLabel>
                <Select
                    displayEmpty
                    labelId="demo-select-small-label"
                    id="demo-select-small"
                    value={selectedStrategy}
                    label="選擇策略"
                    onChange={handleSelectStrategy}
                >
                    {selectedStrategy !=="" ? null: <MenuItem value="">{state?.StrategyTasks[0].strategy_name}</MenuItem>}

                    {
                        strategies.map((strategy) => {
                            return (
                                <MenuItem value={strategy.id }>{strategy.strategy_name}</MenuItem>
                            )
                        })
                    }
                </Select>
            </FormControl>
            <Button variant="contained" onClick={() => {
                console.log(state);
            }}>測試</Button>
        </>

    );
}