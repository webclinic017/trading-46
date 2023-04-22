import Nav from 'react-bootstrap/Nav';
import { Navbar, Container } from "react-bootstrap";
import Sidebar from "react-bootstrap-sidebar-menu";
import { Link } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';

// A Navbar that is always stack in side of the view
function Layout({ children }) {
    return <div className="main-wrapper">{children}</div>;
  }
function Main({ children }) {
    return <main className="main-container container-fluid">{children}</main>;
  }
  
  
function StackedExample() {
    const theme = "dark";
    const navigateTo = useNavigate();

    
    return (
        <Layout >
            <Navbar className="main-header" expand="sm" bg={theme} variant={theme} style={{zIndex:"10"}}>
            <Container fluid>
            <Navbar.Brand href="#home">Brand link</Navbar.Brand>
            </Container>
        </Navbar>
        <Sidebar variant={theme} bg={theme} expand="sm" style={{zIndex:"10"}}>
            <Sidebar.Collapse>
            <Sidebar.Header>
                <Sidebar.Brand>Cool Backtesting</Sidebar.Brand>
                <Sidebar.Toggle />
            </Sidebar.Header>
            <Sidebar.Body>
                <Sidebar.Nav>
                <Sidebar.Nav.Link onSelect={()=>{navigateTo('/makestrategy')}} eventKey="menu_title">
                    <Sidebar.Nav.Icon>1</Sidebar.Nav.Icon>
                    <Sidebar.Nav.Title>自訂義策略</Sidebar.Nav.Title>
                </Sidebar.Nav.Link>
                <Sidebar.Nav.Link onSelect={()=>{navigateTo('/')}} eventKey="multipleBacktest">
                    <Sidebar.Nav.Icon>2</Sidebar.Nav.Icon>
                    <Sidebar.Nav.Title>多股回測</Sidebar.Nav.Title>
                </Sidebar.Nav.Link>
                <Sidebar.Nav.Link onSelect={()=>{navigateTo('/backtest')}} eventKey="multipleDev">
                    <Sidebar.Nav.Icon>3</Sidebar.Nav.Icon>
                    <Sidebar.Nav.Title>開發 BETA</Sidebar.Nav.Title>
                </Sidebar.Nav.Link>
                <Sidebar.Sub eventKey={0}>
                    <Sidebar.Sub.Toggle>
                    <Sidebar.Nav.Icon />
                    <Sidebar.Nav.Title>Submenu</Sidebar.Nav.Title>
                    </Sidebar.Sub.Toggle>
                    <Sidebar.Sub.Collapse>
                    <Sidebar.Nav>
                        {/* linkl to another page */}
                        <Sidebar.Nav.Link onSelect={()=>{navigateTo('/backtest')}}eventKey="sum_menu_title">
                        <Sidebar.Nav.Icon>1.1</Sidebar.Nav.Icon>
                        <Sidebar.Nav.Title>Sub menu item</Sidebar.Nav.Title>
                        </Sidebar.Nav.Link>
                    </Sidebar.Nav>
                    </Sidebar.Sub.Collapse>
                </Sidebar.Sub>
                </Sidebar.Nav>
            </Sidebar.Body>
            </Sidebar.Collapse>
        </Sidebar>
        </Layout>
    )
}

export default StackedExample;