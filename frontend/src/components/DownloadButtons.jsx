import React from 'react';

const DownloadButtons = ({ projectId }) => {
  return (
    <div>
      <button onClick={() => {/* Download CSV */}}>CSV</button>
      <button onClick={() => {/* Download PNG */}}>PNG</button>
      <button onClick={() => {/* Download PDF */}}>PDF</button>
    </div>
  );
};

export default DownloadButtons;
