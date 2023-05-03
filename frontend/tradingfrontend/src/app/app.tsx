import styled from 'styled-components';
import React from 'react';
import NxWelcome from './nx-welcome';
import Dndpage from '../pages/Dndpage';
import Backtest from '../pages/Backtest';
import StackedExample from "src/components/Navbar";
import LeftTabsExample from "src/components/NabarBootstrap";

import SelectStrategy from "src/components/MakeStrategyViewer/SelectStrategy";
import SingleBacktest from "src/pages/SingleBacktest";
import SignIn from "src/pages/SignIn";
import SignUp from "src/pages/SignUp";
import MakeStrategy from "src/pages/MakeStrategy";

import 'bootstrap/dist/css/bootstrap.min.css';
import "src/scss/styles.scss";
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import { StrategyContext } from 'src/components/MakeStrategyContext/StrategyContext'
import { StrategysReducer,SingleBacktestReducer } from 'src/components/MakeStrategyContext/StrategyReducers';
const StyledApp = styled.div`
  // Your style here
`;

export function App() {
  const initialState = {
    StrategyTasks: [],
    SingleBacktest: []
  };
  const mainReducer = ({ StrategyTasks, SingleBacktest }, action) => ({
    StrategyTasks: StrategysReducer(StrategyTasks, action),
    SingleBacktest: SingleBacktestReducer(SingleBacktest, action)
  });
  const [state, dispatch] = React.useReducer(mainReducer, initialState);
  return (
    <StyledApp>
      <StrategyContext.Provider value={{ state, dispatch }}>

        <BrowserRouter>
          <Routes>
            <Route path="/" Component={SignIn} />
            <Route path="/signup" Component={SignUp} />
          </Routes>
          {/* <LeftTabsExample></LeftTabsExample> */}


          <Routes>
            <Route path="/Singlebacktest" element={<><StackedExample /><SingleBacktest /></>} />
            <Route path="/backtest" element={<><StackedExample /><Backtest /></>} />
            <Route path="/makestrategy" element={<><StackedExample /><MakeStrategy /></>} />
          </Routes>
        </BrowserRouter>
        {/* <Dndpage></Dndpage> */}
        {/* <NxWelcome title="tradingfrontend" /> */}
      </StrategyContext.Provider>

    </StyledApp>
  );
}

export default App;
