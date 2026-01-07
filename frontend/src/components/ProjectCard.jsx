import React from 'react';

const ProjectCard = ({ project }) => {
  return (
    <div className="border p-4">
      <h2>{project.name}</h2>
      {/* Link to detail */}
    </div>
  );
};

export default ProjectCard;
