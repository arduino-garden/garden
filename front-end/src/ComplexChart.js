import React from 'react';

import {
  XAxis,
  YAxis,
  FlexibleWidthXYPlot,
  HorizontalGridLines,
  LineSeries,
  VerticalRectSeries,
  DiscreteColorLegend,
  Crosshair
} from 'react-vis';

// /**
//  * Get the array of x and y pairs.
//  * The function tries to avoid too large changes of the chart.
//  * @param {number} total Total number of values.
//  * @returns {Array} Array of data.
//  * @private
//  */

// function getRandomSeriesData(total) {
//   const result = [];
//   let lastY = Math.random() * 40 - 20;
//   let y;
//   const firstY = lastY;
//   for (let i = 0; i < Math.max(total, 3); i++) {
//     y = Math.random() * firstY - firstY / 2 + lastY;
//     result.push({
//       left: i,
//       top: y
//     });
//     lastY = y;
//   }
//   return result;
// }

const data = [
    {x0: 0, x: 1, y: 1},
    {x0: 1, x: 2, y: 2},
    {x0: 2, x: 3, y: 10},
    {x0: 3, x: 4, y: 6},
    {x0: 4, x: 5, y: 5},
    {x0: 5, x: 6, y: 3},
    {x0: 6, x: 7, y: 1}
];  

export default class Example extends React.Component {
  constructor(props) {
    super(props);
   // const totalValues = Math.random() * 50;
    this.state = {
      crosshairValues: [],
      series: [
        {
          title: 'Apples',
          disabled: false,
          data: {data}
        },
        {
          title: 'Bananas',
          disabled: false,
          data: {data}
        }
      ]
    };
  }

//   /**
//    * A callback to format the crosshair items.
//    * @param {Object} values Array of values.
//    * @returns {Array<Object>} Array of objects with titles and values.
//    * @private
//    */
//   _formatCrosshairItems = values => {
//     const {series} = this.state;
//     return values.map((v, i) => {
//       return {
//         title: series[i].title,
//         value: v.top
//       };
//     });
//   };

//   /**
//    * Format the title line of the crosshair.
//    * @param {Array} values Array of values.
//    * @returns {Object} The caption and the value of the title.
//    * @private
//    */
//   _formatCrosshairTitle = values => {
//     return {
//       title: 'X',
//       value: values[0].left
//     };
//   };

//   /**
//    * Click handler for the legend.
//    * @param {Object} item Clicked item of the legend.
//    * @param {number} i Index of the legend.
//    * @private
//    */
//   _legendClickHandler = (item, i) => {
//     const {series} = this.state;
//     series[i].disabled = !series[i].disabled;
//     this.setState({series});
//   };

//   /**
//    * Event handler for onMouseLeave.
//    * @private
//    */
//   _mouseLeaveHandler = () => {
//     this.setState({crosshairValues: []});
//   };

//   /**
//    * Event handler for onNearestX.
//    * @param {Object} value Selected value.
//    * @param {number} index Index of the series.
//    * @private
//    */
//   _nearestXHandler = (value, {index}) => {
//     const {series} = this.state;
//     this.setState({
//       crosshairValues: series.map(s => s.data[index])
//     });
//   };

//   _updateButtonClicked = () => {
//     const {series} = this.state;
//     const totalValues = Math.random() * 50;
//     series.forEach(s => {
//       s.data = getRandomSeriesData(totalValues);
//     });
//     this.setState({series});
//   };

  render() {
    const {data, crosshairValues} = this.state;
    return (
      <div className="example-with-click-me">
        <div className="legend">
          <DiscreteColorLegend
            onItemClick={this._legendClickHandler}
            width={180}
            items={data}
          />
        </div>

        <div className="chart">
          <FlexibleWidthXYPlot
            animation
            getX={d => d.left}
            getY={d => d.top}
            onMouseLeave={this._mouseLeaveHandler}
            xDomain={data}
            height={300}
          >
            <HorizontalGridLines />
            <YAxis
              className="cool-custom-name"
              tickSizeInner={0}
              tickSizeOuter={3}
            />
            <XAxis
              className="even-cooler-custom-name"
              tickSizeInner={0}
              tickSizeOuter={3}
            />
            {/* <VerticalRectSeries
              data={data}
              stroke="white"
              onNearestX={this._nearestXHandler}
            />
            <LineSeries
              data={data}
              curve="curveMonotoneX"
            />
            <Crosshair
              itemsFormat={this._formatCrosshairItems}
              titleFormat={this._formatCrosshairTitle}
              values={crosshairValues}
            /> */}
          </FlexibleWidthXYPlot>
        </div>

        <button className="click-me" onClick={this._updateButtonClicked}>
          Click to update
        </button>
      </div>
    );
  }
}
