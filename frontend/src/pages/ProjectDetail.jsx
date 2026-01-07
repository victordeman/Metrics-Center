import React from 'react';
import FileUpload from '../components/FileUpload';
import GoogleDrivePicker from '../components/GoogleDrivePicker';
import ClusteringForm from '../components/ClusteringForm';
import MetricsTable from '../components/MetricsTable';
import PlotlyChart from '../components/PlotlyChart';
import DownloadButtons from '../components/DownloadButtons';
// Use useParams for projectId

const ProjectDetail = () => {
  // Fetch project data, evaluations
  return (
    <div className="p-4">
      <h1>Project Detail</h1>
      <FileUpload />
      <GoogleDrivePicker />
      <ClusteringForm />
      {/* Display results */}
      <MetricsTable metrics={{}} />
      <PlotlyChart data={{}} />
      <DownloadButtons />
    </div>
  );
};

export default ProjectDetail;
