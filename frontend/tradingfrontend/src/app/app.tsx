import styled from 'styled-components';

import NxWelcome from './nx-welcome';
import Dndpage from '../pages/Dndpage';
import Backtest from '../pages/Backtest';
import StackedExample from "src/components/Navbar";
import LeftTabsExample from "src/components/NabarBootstrap";
import SingleBacktest from "src/pages/SingleBacktest";
import SignIn from "src/pages/SignIn";
import SignUp from "src/pages/SignUp";
import MakeStrategy from "src/pages/MakeStrategy";
import 'bootstrap/dist/css/bootstrap.min.css';
import "src/scss/styles.scss";
import { BrowserRouter, Route, Routes } from 'react-router-dom'

const StyledApp = styled.div`
  // Your style here
`;

export function App() {
  return (
    <StyledApp>
      <BrowserRouter>
        <Routes>
          <Route path="/" Component={SignIn} />
          <Route path="/signup" Component={SignUp} />
        </Routes>
        {/* <LeftTabsExample></LeftTabsExample> */}


        <Routes>
          <Route path="/backtest" element={<><StackedExample />
            <SingleBacktest /></>} />
          <Route path="/backtest" element={<><StackedExample /><Backtest /></>} />
          <Route path="/makestrategy" element={<><StackedExample /><MakeStrategy /></>} />
        </Routes>
      </BrowserRouter>
      {/* <Dndpage></Dndpage> */}
      {/* <NxWelcome title="tradingfrontend" /> */}
    </StyledApp>
  );
}

export default App;
