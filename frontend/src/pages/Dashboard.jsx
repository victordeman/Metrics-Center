import React from 'react';
import { useProjects } from '../hooks/useProjects';
import ProjectCard from '../components/ProjectCard';

const Dashboard = () => {
  const { projects } = useProjects();

  return (
    <div className="p-4">
      <h1>Dashboard</h1>
      <div className="grid grid-cols-3 gap-4">
        {projects.map(project => <ProjectCard key={project.id} project={project} />)}
      </div>
    </div>
  );
};

export default Dashboard;
