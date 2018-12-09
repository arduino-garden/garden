import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import TimeChart from './TimeChart';
import VoronoiLineChart from './VoronoiLineChart'; 
import ZoomableChart from './ZoomableChart';
import * as serviceWorker from './serviceWorker';

ReactDOM.render(<TimeChart />, document.getElementById('root'));
//ReactDOM.render(<VoronoiLineChart />, document.getElementById('root'));
//ReactDOM.render(<ZoomableChart />, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();
