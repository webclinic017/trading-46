import styled from 'styled-components';

import NxWelcome from './nx-welcome';
import Dndpage from '../pages/Dndpage';
import Backtest from '../pages/Backtest';
import StackedExample from "src/components/Navbar";
import LeftTabsExample from "src/components/NavbarBootstrap";
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
        {/* <LeftTabsExample></LeftTabsExample> */}
        <StackedExample></StackedExample>

        <Routes>
          <Route path="/" Component={Backtest} />
        </Routes>
      </BrowserRouter>
      {/* <Dndpage></Dndpage> */}
      {/* <NxWelcome title="tradingfrontend" /> */}
    </StyledApp>
  );
}

export default App;
