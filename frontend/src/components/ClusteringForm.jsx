import React, { useState } from 'react';

const ClusteringForm = ({ onSubmit }) => {
  const [algorithm, setAlgorithm] = useState('KMeans');
  const [hyperparams, setHyperparams] = useState({});

  // Form fields for hyperparams based on algorithm

  return (
    <form onSubmit={() => onSubmit({ algorithm, hyperparams })}>
      {/* Select algorithm, inputs for params */}
      <button type="submit">Run Evaluation</button>
    </form>
  );
};

export default ClusteringForm;
