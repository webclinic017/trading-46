import * as React from 'react';
import { styled } from '@mui/material/styles';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import ChevronRightIcon from '@mui/icons-material/ChevronRight';
import Chip from '@mui/material/Chip';
import TreeView from '@mui/lab/TreeView';
import TreeItem from '@mui/lab/TreeItem';
import AddCircleIcon from '@mui/icons-material/AddCircle';
import ConditionAddList from './ConditionAddList';
import { useState,useEffect } from 'react';
import TextField from '@mui/material/TextField';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import FormControl from '@mui/material/FormControl';
import Select, { SelectChangeEvent } from '@mui/material/Select';
import NativeSelect from '@mui/material/NativeSelect';
import InputLabel from '@mui/material/InputLabel';
import axios from 'axios';

function ControlledTreeView(props: any) {
    const [expanded, setExpanded] = React.useState<string[]>([]);
    const [selected, setSelected] = React.useState<string[]>([]);

    const handleToggle = (event: React.SyntheticEvent, nodeIds: string[]) => {
        setExpanded(nodeIds);
    };

    const handleSelect = (event: React.SyntheticEvent, nodeIds: string[]) => {
        setSelected(nodeIds);
    };

    const handleSendSelected = () => {
        props.handleSelectedFactors(selected)
    }
    const handleExpandClick = () => {
        setExpanded((oldExpanded) =>
            oldExpanded.length === 0 ? ['1', '5', '6', '7'] : [],
        );
    };

    const handleSelectClick = () => {
        setSelected((oldSelected) =>
            oldSelected.length === 0 ? ['1', '2', '3', '4', '5', '6', '7', '8', '9'] : [],
        );
    };

    return (
        <Box sx={{ height: 270, flexGrow: 1, maxWidth: 400, overflowY: 'auto' }}>
            <Box sx={{ mb: 1 }}>
                <Button onClick={handleExpandClick}>
                    {expanded.length === 0 ? 'Expand all' : 'Collapse all'}
                </Button>
                <Button onClick={handleSelectClick}>
                    {selected.length === 0 ? 'Select all' : 'Unselect all'}
                </Button>
            </Box>
            <TreeView
                aria-label="controlled"
                defaultCollapseIcon={<ExpandMoreIcon />}
                defaultExpandIcon={<ChevronRightIcon />}
                expanded={expanded}
                selected={selected}
                onNodeToggle={handleToggle}
                onNodeSelect={handleSelect}
                multiSelect
            >
                <TreeItem nodeId="1" label="技術指標">
                    <TreeItem nodeId="均線" label="均線" >
                            <TreeItem nodeId="5日均線" label="5日均線" />
                            <TreeItem nodeId="10日均線" label="10日均線" />
                            <TreeItem nodeId="15日均線" label="15日均線" />
                            <TreeItem nodeId="20日均線" label="20日均線" />
                            <TreeItem nodeId="25日均線" label="25日均線" />
                            <TreeItem nodeId="30日均線" label="30日均線" />
                            <TreeItem nodeId="60日均線" label="60日均線" />
                            <TreeItem nodeId="120日均線" label="120日均線" />

                    </TreeItem>
                    <TreeItem nodeId="收盤價" label="收盤價" />
                    <TreeItem nodeId="KD" label="KD" />
                </TreeItem>
                {/* <TreeItem nodeId="5" label="Documents">
                    <TreeItem nodeId="6" label="MUI">
                        <TreeItem nodeId="7" label="src">
                            <TreeItem nodeId="8" label="index.js" />
                            <TreeItem nodeId="9" label="tree-view.js" />
                        </TreeItem>
                    </TreeItem>
                </TreeItem> */}
            </TreeView>
            <Box sx={{ mb: 1 }}>
                <Button onClick={handleSendSelected}>
                    增加指標
                </Button>
            </Box>
        </Box>
    );
}
function ConditionBoard(props) {
    const handleClick = () => {
        console.info('You clicked the Chip.');
    };

    const handleDelete = (chip) => {
        props.handleDeleteSelectedFactors(chip)
        console.info('You clicked the delete icon.');
        console.log(props.displayChips)
    };

    return (
        <Box sx={{ width: '100%', maxWidth: 360, bgcolor: 'background.paper' }}>
        {/* <Stack direction="row" spacing={1}  > */}
            {props.displayChips.map((chip) => (
                <Chip
                    label={chip}
                    onClick={handleClick}
                    onDelete={()=>{handleDelete(chip)}}
    
                    // deleteIcon={<AddCircleIcon />}
                />
            ))
            }
        {/* </Stack> */}
        </Box>
    );
}
export default function MakeStrategyBoard() {
    const [SingleBacktest, setSingleBacktest] = React.useState([]);
    const handleSingleBacktest = (data) => {
        setSingleBacktest(data)
        console.log(SingleBacktest, 'SingleBacktest')
    }
    const [selectedFactors, setSelectedFactors] = React.useState<string[]>([]);
    const handleSelectedFactors = (nodeIds) => {
        let selectedFactorsWithoutDuplicate = [...new Set([...selectedFactors, ...nodeIds])]
        setSelectedFactors(selectedFactorsWithoutDuplicate)
        console.log(nodeIds)
    }
    const handleDeleteSelectedFactors = (nodeIds) => {
        let selectedFactorsRemoveList = selectedFactors.filter((item) => !nodeIds.includes(item))
        setSelectedFactors(selectedFactorsRemoveList)
        console.log(nodeIds)
    }



    
    //以下為暫時用來測試的資料
    async function login(username, password) {
        const data = {
            'email': username,
            'password': password
        }
        await axios.post('http://localhost:8050/api/v1/auth/login', data).then(response => {
            console.log(response.data);
            localStorage.setItem('access_token', response.data.access_token);
        }
        ).catch(error => {
            console.log(error);
        });
    }
    useEffect(() => {
        login('test01@example.com', '123456');
    }, []);
    const [all_data, setAll_data] = useState({
        'stock_symbol': '2033',
        'strategy_id': '6440e166e21de61de0e59e50',
        'buy_strategy': 'self.buy_pct = 0.5ChangeLine                self.sell_pct = 1',
        'sell_strategy': 'if backtesting.lib.crossover(self.ma10, self.ma20): self.buy()ChangeLine                elif backtesting.lib.crossover(self.ma20, self.ma10): self.sell()',
        'plot': 'true',
        'start_date': '2020-01-05',
        'end_date': '2023-02-18',
        'cash': '10000000',
        'commission': '0.00145'
    });
    useEffect(() => {
        console.log(all_data);
    }, [all_data]);
    let isTrueSet = (all_data.plot === 'true');
    const [response, setResponse] = useState("");
    async function single_test_with_custom_strategy() {
        const data = {
            'stock_symbol': all_data.stock_symbol,
            'strategy_id': all_data.strategy_id,
            'buy_strategy': all_data.buy_strategy,
            'sellstrategy': all_data.sell_strategy,
            'plot': isTrueSet,
            'start_date': all_data.start_date,
            'end_date': all_data.end_date,
            'cash': parseFloat(all_data.cash),
            'commission': parseFloat(all_data.commission)
        }
        console.log(data);
        const config = {
            headers: { Authorization: `Bearer ${localStorage.getItem('access_token')}` }
        };
        
        await axios.post('http://localhost:8050/api/v1/backtest/single_backtesting_with_custom_strategy', data, config).then(response => {
            console.log(response.data);
            setResponse(response.data.date);
        }
        ).catch(error => {
            console.log(error);
        });
    }
    // http://localhost:4041/htmlplots/test01@example.com_asd_2330.html
    let backtest_str = `http://localhost:4041/htmlplots/test01@example.com_asd_${all_data.stock_symbol}.html`;
    console.log(backtest_str)


    return (
        <>
            <Stack direction="row" sx={{width:'100%'}} >
                <Stack direction="column" spacing={1} >
                <Box  >
                    <Typography component="div" variant="h10">
                        自訂指標
                    </Typography>
                    <ConditionBoard displayChips={selectedFactors} handleDeleteSelectedFactors={handleDeleteSelectedFactors} />
                </Box>
                <Box >
                    <Typography component="div" variant="h10">
                        指標條件
                    </Typography>
                    {/* <Button >
                        新增買進賣出條件
                </Button> */}
                <Stack direction="column" spacing={1} >
                    <Box style={{width:'100%'}} >
                        {/* <Typography component="div" variant="h10">
                            買賣條件
                        </Typography> */}
                        <ConditionAddList selectedFactors={selectedFactors} handleSingleBacktest={handleSingleBacktest} />
                    </Box>
                    <Box style={{width:'100%'}} >
                        <Typography component="div" variant="h10">
                            條件順序拖動
                        </Typography>
                    </Box>
                </Stack>
                </Box>
                
                </Stack>
                <Box style={{ width: "50%" }}>
                    <ControlledTreeView handleSelectedFactors={handleSelectedFactors} />
                </Box>
            </Stack>
            {/* <Box sx={{ mb: 1 }}>
                <Button >
                    新增策略
                </Button>
                <Button >
                    及時回測
                </Button>
            </Box> */}
        </>

    )


}
{/* <Card sx={{ display: 'flex' }}>
                <Typography component="div" sx={{ display: 'flex', flexDirection: 'column' }}>
                    <CardContent sx={{ flex: '1 0 auto' }}>
                        <Typography component="div" variant="h5">
                            Single Back Test
                        </Typography>
                        <Typography variant="subtitle1" color="text.secondary" component="div">
                            Oscar Yuh
                        </Typography>
                    </CardContent>
                    <Box sx={{ display: 'flex', flexDirection: 'column' }}>
                        <TextField
                            id="outlined-multiline-flexible"
                            label="stock_symbol"
                            multiline
                            InputLabelProps={{
                                shrink: true,
                              }}
                            value={all_data.stock_symbol}
                            onChange={(e) => setAll_data({ ...all_data, stock_symbol: e.target.value })}
                        >
                        </TextField>
                        <TextField
                            id="outlined-multiline-flexible"
                            label="strategy_id"
                            multiline
                            InputLabelProps={{
                                shrink: true,
                              }}
                            value={all_data.strategy_id}
                            onChange={(e) => setAll_data({ ...all_data, strategy_id: e.target.value })}
                        >
                        </TextField>
                        <TextField
                            id="outlined-multiline-flexible"
                            label="buy_strategy"
                            multiline
                            value={all_data.buy_strategy}
                            maxRows={4}
                            InputLabelProps={{
                                shrink: true,
                              }}
                            onChange={(e) => setAll_data({ ...all_data, buy_strategy: e.target.value })}
                            >
                            
                        </TextField>
                        <TextField
                            id="outlined-multiline-flexible"
                            label="sell_strategy"
                            multiline
                            value={all_data.sell_strategy}
                            maxRows={4}
                            InputLabelProps={{
                                shrink: true,
                              }}
                            onChange={(e) => setAll_data({ ...all_data, sell_strategy: e.target.value })}
                            >
                        </TextField>
                        <Box sx={{ minWidth: 120 }}>
                            <FormControl fullWidth>
                                <InputLabel variant="standard" htmlFor="uncontrolled-native">
                                    plot
                                </InputLabel>
                                <NativeSelect
                                    defaultValue={30}
                                    inputProps={{
                                        name: 'age',
                                        id: 'uncontrolled-native',
                                    }}
                                    onChange={(e) => setAll_data({ ...all_data, plot: e.target.value })}
                                >
                                    <option value={'true'}>True</option>
                                    <option value={'false'}>False</option>
                                </NativeSelect>
                            </FormControl>
                        </Box>
                        <TextField
                            id="outlined-multiline-flexible"
                            label="start_date"
                            multiline
                            InputLabelProps={{
                                shrink: true,
                              }}
                            value={all_data.start_date}
                            onChange={(e) => setAll_data({ ...all_data, start_date: e.target.value })}
                        >
                        </TextField>
                        <TextField
                            id="outlined-multiline-flexible"
                            label="end_date"
                            multiline
                            value={all_data.end_date}
                            InputLabelProps={{
                                shrink: true,
                              }}
                            onChange={(e) => setAll_data({ ...all_data, end_date: e.target.value })}
                        >
                        </TextField>
                        <TextField
                            id="outlined-multiline-flexible"
                            label="cash"
                            multiline
                            InputLabelProps={{
                                shrink: true,
                              }}
                            value={all_data.cash}
                            onChange={(e) => setAll_data({ ...all_data, cash: e.target.value })}
                        >
                        </TextField>
                        <TextField
                            id="outlined-multiline-flexible"
                            label="commission"
                            multiline
                            InputLabelProps={{
                                shrink: true,
                              }}
                            value={all_data.commission}
                            onChange={(e) => setAll_data({ ...all_data, commission: e.target.value })}
                        >
                        </TextField>
                        <Button variant="contained" onClick={()=>{single_test_with_custom_strategy()}}>Single Back Test</Button>
                        {response}
                        <iframe title= "cool" src= {backtest_str} width="700px" height="500px"></iframe>
                    </Box>
                </Typography>
            </Card> */}