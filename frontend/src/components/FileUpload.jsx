import React from 'react';

const FileUpload = ({ onUpload }) => {
  return (
    <input type="file" onChange={onUpload} className="block" />
  );
};

export default FileUpload;
