import React from 'react';

import {
  XYPlot,
  XAxis,
  YAxis,
  HorizontalGridLines,
  VerticalGridLines,
  LineSeries,
  MarkSeries,
  Voronoi
} from 'react-vis';

const lines = [
  [{x: 1, y: 3}, {x: 2, y: 5}, {x: 3, y: 15}, {x: 4, y: 12}],
  [{x: 1, y: 10}, {x: 2, y: 4}, {x: 3, y: 2}, {x: 4, y: 15}],
  [{x: 1, y: 7}, {x: 2, y: 11}, {x: 3, y: 9}, {x: 4, y: 2}]
].map((p, i) => p.map(d => ({...d, line: i})));
const nodes = lines.reduce((acc, d) => [...acc, ...d], []);

const getDomain = (data, key) => {
  const {min, max} = data.reduce(
    (acc, row) => ({
      min: Math.min(acc.min, row[key]),
      max: Math.max(acc.max, row[key])
    }),
    {min: Infinity, max: -Infinity}
  );
  return [min, max];
};
const xDomain = getDomain(nodes, 'x');
const yDomain = getDomain(nodes, 'y');

export default class VoronoiLineChart extends React.Component {
  state = {
    hoveredNode: null,
    showVoronoi: false
  };

  render() {
    const {hoveredNode, showVoronoi} = this.state;
    return (
      <div>
        <label style={{display: 'block'}}>
          <input
            type="checkbox"
            checked={showVoronoi}
            onChange={e => this.setState({showVoronoi: !showVoronoi})}
          />
          Show Voronoi
        </label>
        <XYPlot
          xDomain={xDomain}
          yDomain={yDomain}
          margin={{top: 10, left: 40, bottom: 40, right: 10}}
          width={300}
          height={300}
        >
          <HorizontalGridLines />
          <VerticalGridLines />
          <XAxis title="X Axis" />
          <YAxis title="Y Axis" />
          {lines.map((d, i) => (
            <LineSeries
              key={i}
              opacity={hoveredNode && hoveredNode.line === i ? 1 : 0.5}
              data={d}
            />
          ))}
          {hoveredNode && <MarkSeries data={[hoveredNode]} />}
          <Voronoi
            nodes={lines.reduce((acc, d) => [...acc, ...d], [])}
            onHover={node => this.setState({hoveredNode: node})}
            onBlur={() => this.setState({hoveredNode: null})}
            polygonStyle={{stroke: showVoronoi ? 'rgba(0, 0, 0, .2)' : null}}
          />
        </XYPlot>
      </div>
    );
  }
}