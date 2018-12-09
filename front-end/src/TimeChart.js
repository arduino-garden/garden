import React, { Component } from 'react';
import './App.css';
import '../node_modules/react-vis/dist/style.css';

import {
    XYPlot,
    XAxis,
    YAxis,
    HorizontalGridLines,
    VerticalGridLines,
    LineSeries
} from 'react-vis';

const MSEC_DAILY = 86400000;

export default function TimeChart(props) {
    const timestamp = new Date().getTime() - 5 * MSEC_DAILY;

    // var days = 3; // Days you want to subtract
    // var date = new Date();
    // var last = new Date(date.getTime() - (days * 24 * 60 * 60 * 1000));
    // var day = last.getDate();
    // var month = last.getMonth() + 1;

    // var timestamp = month + ' ' + day;

    //var timestamp = new Date(new Date().getTime() + 86400 + 3);
    // d.setDate(d.getDate()-5);
    // let timestamp = date + month; 
    // let date = currentDate.getDate();
    // let month = currentDate.getMonth();
    // let timestamp = date + '/' + month;
    // date.setDate(date.getDate() - 7);
    // var timestamp = date.getDate() + (date.getMonth() + 1);

    return (
        <XYPlot xType="time" width={600} height={400}>
            <HorizontalGridLines />
            <VerticalGridLines />
            <XAxis title="X Axis" />
            <YAxis title="Y Axis" />
            <LineSeries
                data={[
                    { x: timestamp + MSEC_DAILY, y: 3 },
                    { x: timestamp + MSEC_DAILY * 2, y: 5 },
                    { x: timestamp + MSEC_DAILY * 3, y: 15 },
                    { x: timestamp + MSEC_DAILY * 4, y: 12 }
                ]}
            />
            <LineSeries data={null} />
            <LineSeries
                data={[
                    { x: timestamp + MSEC_DAILY, y: 10 },
                    { x: timestamp + MSEC_DAILY * 2, y: 4 },
                    { x: timestamp + MSEC_DAILY * 3, y: 2 },
                    { x: timestamp + MSEC_DAILY * 4, y: 15 }
                ]}
            />
            <LineSeries
                data={[
                    { x: timestamp + MSEC_DAILY, y: 15 },
                    { x: timestamp + MSEC_DAILY * 2, y: 6 },
                    { x: timestamp + MSEC_DAILY * 3, y: 10 },
                    { x: timestamp + MSEC_DAILY * 4, y: 17 }
                ]}
            />
        </XYPlot>
    );
}
