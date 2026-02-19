import React, { useState, useEffect } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;

  useEffect(() => {
    console.log('Teams: fetching from', apiUrl);
    fetch(apiUrl)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        console.log('Teams: fetched data', data);
        // Support both paginated (.results) and plain array responses
        const items = Array.isArray(data) ? data : data.results || [];
        setTeams(items);
        setLoading(false);
      })
      .catch((err) => {
        console.error('Teams: fetch error', err);
        setError(err.message);
        setLoading(false);
      });
  }, [apiUrl]);

  if (loading) {
    return (
      <div className="container octofit-loading">
        <div className="spinner-border text-success me-3" role="status" aria-hidden="true"></div>
        <span className="fs-5">Loading teams...</span>
      </div>
    );
  }

  if (error) {
    return (
      <div className="container mt-4">
        <div className="alert alert-danger d-flex align-items-center" role="alert">
          <strong>Error:&nbsp;</strong> {error}
        </div>
      </div>
    );
  }

  return (
    <div className="container">
      <div className="card octofit-card">
        <div className="card-header d-flex align-items-center justify-content-between">
          <h2 className="mb-0">👥 Teams</h2>
          <span className="badge bg-secondary">{teams.length} teams</span>
        </div>
        <div className="card-body p-0">
          <div className="table-responsive">
            <table className="table table-striped table-bordered table-hover octofit-table mb-0">
              <thead>
                <tr>
                  <th scope="col">#</th>
                  <th scope="col">Team Name</th>
                  <th scope="col">Members</th>
                  <th scope="col">Count</th>
                </tr>
              </thead>
              <tbody>
                {teams.length === 0 ? (
                  <tr>
                    <td colSpan="4" className="text-center text-muted py-4">No teams found.</td>
                  </tr>
                ) : (
                  teams.map((team, idx) => {
                    const memberList = Array.isArray(team.members)
                      ? team.members
                      : team.members
                        ? String(team.members).split(',').map((m) => m.trim())
                        : [];
                    return (
                      <tr key={team._id || team.id}>
                        <td className="text-muted">{idx + 1}</td>
                        <td className="fw-semibold">{team.name}</td>
                        <td>
                          {memberList.map((m, i) => (
                            <span key={i} className="badge bg-info text-dark me-1 mb-1">{m}</span>
                          ))}
                        </td>
                        <td>
                          <span className="badge bg-secondary">{memberList.length}</span>
                        </td>
                      </tr>
                    );
                  })
                )}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Teams;
