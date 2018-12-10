import React from 'react';

import {
  XYPlot,
  XAxis,
  VerticalGridLines,
  HorizontalGridLines,
  LineSeries,
  Highlight
} from 'react-vis';

export default class ZoomableChartWithHover extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      lastDrawLocation: null,
      selectedIndex: null,
      series: [
        {
          disabled: false,
          title: 'Apples'
        },
        {
          disabled: false,
          title: 'Bananas'
        }
      ]
    };
    this._onSeriesMouseOvers = [
      this._onSeriesMouseOver.bind(this, 0),
      this._onSeriesMouseOver.bind(this, 1),
      this._onSeriesMouseOver.bind(this, 2)
    ];
  }

  _getSeriesColor(index) {
    const { selectedIndex } = this.state;
    if (selectedIndex !== null && selectedIndex !== index) {
      return '#ddd';
    }
    return null;
  }

  _onChartMouseLeave = () => {
    this.setState({ selectedIndex: null });
  };

  _onSeriesMouseOver(selectedIndex) {
    this.setState({ selectedIndex });
  }

  render() {
    const { lastDrawLocation } = this.state;
    return (
      <div>
        <XYPlot
          onMouseLeave={this._onChartMouseLeave}
          animation
          xDomain={
            lastDrawLocation && [
              lastDrawLocation.left,
              lastDrawLocation.right
            ]
          }
          yDomain={
            lastDrawLocation && [
              lastDrawLocation.bottom,
              lastDrawLocation.top
            ]
          }
          width={700}
          height={300}
        >
          <VerticalGridLines />
          <HorizontalGridLines />
          <XAxis />
          <Highlight
            onBrushEnd={area => this.setState({ lastDrawLocation: area })}
            onDrag={area => {
              this.setState({
                lastDrawLocation: {
                  bottom: lastDrawLocation.bottom + (area.top - area.bottom),
                  left: lastDrawLocation.left - (area.right - area.left),
                  right: lastDrawLocation.right - (area.right - area.left),
                  top: lastDrawLocation.top + (area.top - area.bottom)
                }
              });
            }}
          />
          <LineSeries
            color={this._getSeriesColor(0)}
            onSeriesMouseOver={this._onSeriesMouseOvers[0]}
            data={[{ x: 1, y: 4 }, { x: 2, y: 11 }, { x: 3, y: 9 }]}
          />
          <LineSeries
            color={this._getSeriesColor(1)}
            onSeriesMouseOver={this._onSeriesMouseOvers[1]}
            data={[{ x: 1, y: 2 }, { x: 2, y: 3 }, { x: 3, y: 11 }]}
          />
          <LineSeries
            color={this._getSeriesColor(2)}
            onSeriesMouseOver={this._onSeriesMouseOvers[2]}
            data={[{ x: 1, y: 5 }, { x: 2, y: 10 }, { x: 3, y: 20 }]}
          />
        </XYPlot>
        <button
          className="showcase-button"
          onClick={() => this.setState({ lastDrawLocation: null })}
        >
          Reset Zoom
        </button>

        <div>
          <h4>
            <b>Last Draw Area</b>
          </h4>
          {lastDrawLocation ? (
            <ul style={{ listStyle: 'none' }}>
              <li>
                <b>Top:</b> {lastDrawLocation.top}
              </li>
              <li>
                <b>Right:</b> {lastDrawLocation.right}
              </li>
              <li>
                <b>Bottom:</b> {lastDrawLocation.bottom}
              </li>
              <li>
                <b>Left:</b> {lastDrawLocation.left}
              </li>
            </ul>
          ) : (
              <span>Zoom Please!</span>
            )}
        </div>
      </div>
    );
  }
}
