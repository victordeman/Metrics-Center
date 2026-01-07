import React from 'react';

const MetricsTable = ({ metrics }) => {
  return (
    <table className="table-auto">
      <thead>
        <tr><th>Metric</th><th>Value</th></tr>
      </thead>
      <tbody>
        {Object.entries(metrics).map(([key, value]) => (
          <tr key={key}><td>{key}</td><td>{value}</td></tr>
        ))}
      </tbody>
    </table>
  );
};

export default MetricsTable;
