import React from 'react';
import Plot from 'react-plotly.js';

const PlotlyChart = ({ data }) => {
  return <Plot data={data.data} layout={data.layout} />;
};

export default PlotlyChart;
