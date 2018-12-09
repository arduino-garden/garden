import React from 'react';
import ReactDOM from 'react-dom';
import TimeChart from './charts/TimeChart';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<TimeChart />, div);
  ReactDOM.unmountComponentAtNode(div);
});
