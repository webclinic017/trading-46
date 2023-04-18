import React from 'react';
import "../node_modules/bootstrap/dist/css/bootstrap.min.css";



const Backtest = () => {
    return (
        <div>
          <h1 className="text-center" style={{margin:'40px'}}>Welcome</h1>
          
          <div className="container">
               <div className="row">
                   <div className="col">
                     <div className="card text-center" style={{width: '18rem' }}>
                        <img src="https://picsum.photos/seed/picsum/200/300" className="card-img-top" alt="..."/>
                        <div className="card-body">
                          <h5 className="card-title">Card title</h5>
                          <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                          <a href="#" className="btn btn-primary">Go somewhere</a>
                        </div>
                      </div>
                   </div>
                   <div className="col">
                     <div className="card text-center" style={{width: '18rem' }} >
                        <img src="https://picsum.photos/200/300?grayscale" className="card-img-top" alt="..."/>
                        <div className="card-body">
                          <h5 className="card-title">Card title</h5>
                          <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                          <a href="#" className="btn btn-primary">Go somewhere</a>
                        </div>
                      </div>
                   </div>
                   <div className="col">
                     <div className="card text-center" style={{width: '18rem' }} >
                        <img src="https://picsum.photos/seed/picsum/200/300" className="card-img-top" alt="..."/>
                        <div className="card-body">
                          <h5 className="card-title">Card title</h5>
                          <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                          <a href="#" className="btn btn-primary ">Go somewhere</a>
                        </div>
                      </div>
                   </div>
               </div>
          </div>      
        </div>
    )
}

export default Backtest;