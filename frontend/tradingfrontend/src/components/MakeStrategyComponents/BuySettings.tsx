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
import BuyConditionAddList from './BuyConditionAddList';
import { useState, useEffect, useContext } from 'react';
import TextField from '@mui/material/TextField';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import FormControl from '@mui/material/FormControl';
import Select, { SelectChangeEvent } from '@mui/material/Select';
import NativeSelect from '@mui/material/NativeSelect';
import InputLabel from '@mui/material/InputLabel';
import axios from 'axios';
import { StrategyContext } from '../MakeStrategyContext/StrategyContext';
import {
  Types,
  BacktestTypes,
  StrategyTypes,
} from '../MakeStrategyContext/StrategyReducers';
import SwipeableViews from 'react-swipeable-views';
import { useTheme } from '@mui/material/styles';
import BacktestSettings from './BacktestSettings';
import { v4 as uuidv4 } from 'uuid';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';

function ControlledTreeView(props: any) {
  const { state, dispatch } = React.useContext(StrategyContext);
  const [expanded, setExpanded] = React.useState<string[]>([]);
  const [selected, setSelected] = React.useState<string[]>([]);

  let uuid = state?.StrategyTasks[0]?.strategy_id;
  const handleCreatStrategyButton = () => {
    dispatch({
      type: Types.Create,
      payload: {
        strategy_id: uuid,
        strategy_name: 'temp',
        strategy_description: 'temp',
        strategy_code: {
          init_indicators: [],
          stop_loss: 'temp',
          take_profit: 'temp',
          buy_first: 'temp',
          buy_signals: [],
          sell_signals: [],
        },
        Strategy_type: 'temp',
        strategy_parameters: [],
        strategy_author: 'temp',
        strategy_status: 'temp',
        strategy_created_date: 'temp',
        strategy_updated_date: 'temp',
      },
    });
    console.log(state);
  };
  const handleAddBuyAndIndicator = () => {
    dispatch({
      type: StrategyTypes.ADD_BUY_INDICATOR,
      payload: {
        strategy_id: uuid,
        buy_and_indicator: {
          id: uuidv4(),
          category: "standard",
          type: 'and',
          indicator_1: 'id1',
          compare_operator: '>',
          indicator_2: 'id2',
          buyOrSell: 'buy',
          amount: 0,
          unit: 'percent',
        }
      },
    });
    console.log(state);
  };
  const handleAddBuyOrIndicator = () => {
    dispatch({
      type: StrategyTypes.ADD_BUY_INDICATOR,
      payload: {
        strategy_id: uuid,
        buy_and_indicator: {
          id: uuidv4(),
          category: "standard",
          type: 'or',
          indicator_1: 'id1',
          compare_operator: '>',
          indicator_2: 'id2',
          buyOrSell: 'buy',
          amount: 0,
          unit: 'percent',
        }
      },
    });
    console.log(state);
  };
  const handleAddBuyLiveIndicator = () => {
    dispatch({
      type: StrategyTypes.ADD_BUY_INDICATOR,
      payload: {
        strategy_id: uuid,
        buy_and_indicator: {
          id: uuidv4(),
          category: "standard",
          type: 'live',
          indicator_1: 'id1',
          compare_operator: '>',
          indicator_2: 'id2',
          buyOrSell: 'buy',
          amount: 0,
          unit: 'percent',
        }
      },
    });
    console.log(state);
  };

  const handleToggle = (event: React.SyntheticEvent, nodeIds: string[]) => {
    setExpanded(nodeIds);
  };

  const handleSelect = (event: React.SyntheticEvent, nodeIds: string[]) => {
    setSelected(nodeIds);
  };

  //   const handleAddBuyAndIndicator = () => {
  //     dispatch({
  //         type: StrategyTypes.ADD_BUY_AND_INDICATOR,
  //         payload: {
  //             id: uuidv4(),

  const handleSendSelected = () => {
    props.handleSelectedFactors(selected);
  };
  const handleExpandClick = () => {
    setExpanded((oldExpanded) =>
      oldExpanded.length === 0 ? ['1', '5', '6', '7'] : []
    );
  };

  const handleSelectClick = () => {
    setSelected((oldSelected) =>
      oldSelected.length === 0
        ? ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        : []
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
          <TreeItem nodeId="均線" label="均線">
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
        <Button onClick={handleCreatStrategyButton}>新增策略</Button>
        <Button onClick={handleAddBuyAndIndicator}>增加至符合全部</Button>
        <Button onClick={handleAddBuyOrIndicator}>增加至符合指定</Button>
        <Button onClick={handleAddBuyLiveIndicator}>增加至盤中符合</Button>
      </Box>
    </Box>
  );
}
function ConditionBoard(props) {
  const handleClick = () => {
    console.info('You clicked the Chip.');
  };

  const handleDelete = (chip) => {
    props.handleDeleteSelectedFactors(chip);
    console.info('You clicked the delete icon.');
    console.log(props.displayChips);
  };

  return (
    <Box sx={{ width: '100%', maxWidth: 360, bgcolor: 'background.paper' }}>
      {/* <Stack direction="row" spacing={1}  > */}
      {props.displayChips.map((chip) => (
        <Chip
          label={chip}
          onClick={handleClick}
          onDelete={() => {
            handleDelete(chip);
          }}

        // deleteIcon={<AddCircleIcon />}
        />
      ))}
      {/* </Stack> */}
    </Box>
  );
}
export default function BuySettings() {
  const { state, dispatch } = React.useContext(StrategyContext);
  const [expanded, setExpanded] = React.useState<string[]>([]);
  const [selected, setSelected] = React.useState<string[]>([]);

  let uuid = state?.StrategyTasks[0]?.strategy_id;
  const handleCreatStrategyButton = () => {
    dispatch({
      type: Types.Create,
      payload: {
        strategy_id: uuid,
        strategy_name: 'temp',
        strategy_description: 'temp',
        strategy_code: {
          init_indicators: [],
          stop_loss: 'temp',
          take_profit: 'temp',
          buy_first: 'temp',
          buy_signals: [],
          sell_signals: [],
        },
        Strategy_type: 'temp',
        strategy_parameters: [],
        strategy_author: 'temp',
        strategy_status: 'temp',
        strategy_created_date: 'temp',
        strategy_updated_date: 'temp',
      },
    });
    console.log(state);
  };
  const handleAddBuyAndIndicator = () => {
    dispatch({
      type: StrategyTypes.ADD_BUY_INDICATOR,
      payload: {
        strategy_id: uuid,
        buy_and_indicator: {
          id: uuidv4(),
          category: "standard",
          type: 'and',
          indicator_1: 'id1',
          compare_operator: '>',
          indicator_2: 'id2',
          buyOrSell: 'buy',
          amount: 0,
          unit: 'percent',
        }
      },
    });
    console.log(state);
  };
  const handleAddBuyOrIndicator = () => {
    dispatch({
      type: StrategyTypes.ADD_BUY_INDICATOR,
      payload: {
        strategy_id: uuid,
        buy_and_indicator: {
          id: uuidv4(),
          category: "standard",
          type: 'or',
          indicator_1: 'id1',
          compare_operator: '>',
          indicator_2: 'id2',
          buyOrSell: 'buy',
          amount: 0,
          unit: 'percent',
        }
      },
    });
    console.log(state);
  };
  const handleAddBuyLiveIndicator = () => {
    dispatch({
      type: StrategyTypes.ADD_BUY_INDICATOR,
      payload: {
        strategy_id: uuid,
        buy_and_indicator: {
          id: uuidv4(),
          category: "standard",
          type: 'live',
          indicator_1: 'id1',
          compare_operator: '>',
          indicator_2: 'id2',
          buyOrSell: 'buy',
          amount: 0,
          unit: 'percent',
        }
      },
    });
    console.log(state);
  };

  const [buyOrSell, setBuyOrSell] = React.useState('buy');
  console.log(state, 'state');

  const [SingleBacktest, setSingleBacktest] = React.useState([]);
  const handleSingleBacktest = (data) => {
    setSingleBacktest(data);
    console.log(SingleBacktest, 'SingleBacktest');
  };
  const [selectedFactors, setSelectedFactors] = React.useState<string[]>([]);
  const handleSelectedFactors = (nodeIds) => {
    let selectedFactorsWithoutDuplicate = [
      ...new Set([...selectedFactors, ...nodeIds]),
    ];
    setSelectedFactors(selectedFactorsWithoutDuplicate);
    console.log(nodeIds);
  };
  const handleDeleteSelectedFactors = (nodeIds) => {
    let selectedFactorsRemoveList = selectedFactors.filter(
      (item) => !nodeIds.includes(item)
    );
    setSelectedFactors(selectedFactorsRemoveList);
    console.log(nodeIds);
  };

  return (
    <Box sx={{ width: '100%' }}>
      <Stack direction="row" sx={{ width: '100%' }}>
        <Stack direction="column" spacing={1}>
          <Box>
            {/* <Typography component="div" variant="h10">
              自訂指標
            </Typography> */}
            {/* <ConditionBoard
              displayChips={selectedFactors}
              handleDeleteSelectedFactors={handleDeleteSelectedFactors}
            /> */}
          </Box>
          <Box>
            {/* <Button >
                        新增買進賣出條件
                </Button> */}
            <Stack direction="column" spacing={1} sx={{alignSelf:'center',width:'100%', justifyContent:'center'}}>

              {/* <Box sx={{ mb: 1 }}>
                <Button onClick={handleCreatStrategyButton}>新增策略</Button>
                <Button onClick={handleAddBuyAndIndicator}>增加至符合全部</Button>
                <Button onClick={handleAddBuyOrIndicator}>增加至符合指定</Button>
                <Button onClick={handleAddBuyLiveIndicator}>增加至盤中符合</Button>
              </Box> */}
              <Box style={{ width: '100%', }}>
                {/* <Typography component="div" variant="h10">
                            買賣條件
                        </Typography> */}
                <BuyConditionAddList
                  selectedFactors={selectedFactors}
                  handleSingleBacktest={handleSingleBacktest}
                />
              </Box>
              {/* <Box style={{width:'100%'}} >
                        <Typography component="div" variant="h10">
                            條件順序拖動
                        </Typography>
                    </Box> */}
            </Stack>
          </Box>
        </Stack>
        {/* <Box style={{ width: '50%' }}>
          <ControlledTreeView buyOrSell={buyOrSell} />
        </Box> */}
      </Stack>
    </Box>
  );
}
