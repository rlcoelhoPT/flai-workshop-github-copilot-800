import React, { useState, useEffect } from 'react';

const rankLabel = (rank) => {
  if (rank === 1) return '🥇 1st';
  if (rank === 2) return '🥈 2nd';
  if (rank === 3) return '🥉 3rd';
  return `${rank}th`;
};

const rankBadgeStyle = (rank) => {
  if (rank === 1) return { backgroundColor: '#ffd700', color: '#333' };
  if (rank === 2) return { backgroundColor: '#c0c0c0', color: '#333' };
  if (rank === 3) return { backgroundColor: '#cd7f32', color: '#fff' };
  return {};
};

function Leaderboard() {
  const [entries, setEntries] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;

  useEffect(() => {
    console.log('Leaderboard: fetching from', apiUrl);
    fetch(apiUrl)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        console.log('Leaderboard: fetched data', data);
        const items = Array.isArray(data) ? data : data.results || [];
        setEntries(items);
        setLoading(false);
      })
      .catch((err) => {
        console.error('Leaderboard: fetch error', err);
        setError(err.message);
        setLoading(false);
      });
  }, [apiUrl]);

  if (loading) {
    return (
      <div className="container octofit-loading">
        <div className="spinner-border text-warning me-3" role="status" aria-hidden="true"></div>
        <span className="fs-5">Loading leaderboard...</span>
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
          <h2 className="mb-0">🏆 Leaderboard</h2>
          <span className="badge bg-secondary">{entries.length} entries</span>
        </div>
        <div className="card-body p-0">
          <div className="table-responsive">
            <table className="table table-striped table-bordered table-hover octofit-table mb-0">
              <thead>
                <tr>
                  <th scope="col">Rank</th>
                  <th scope="col">User</th>
                  <th scope="col">Score</th>
                </tr>
              </thead>
              <tbody>
                {entries.length === 0 ? (
                  <tr>
                    <td colSpan="3" className="text-center text-muted py-4">No entries found.</td>
                  </tr>
                ) : (
                  entries.map((entry, index) => (
                    <tr key={entry._id || entry.id}>
                      <td>
                        <span
                          className="badge rounded-pill"
                          style={{ ...rankBadgeStyle(index + 1), fontSize: '0.85rem', padding: '0.4em 0.7em' }}
                        >
                          {rankLabel(index + 1)}
                        </span>
                      </td>
                      <td className="fw-semibold">{entry.user}</td>
                      <td>
                        <span className="badge bg-success fs-6">{entry.score}</span>
                      </td>
                    </tr>
                  ))
                )}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Leaderboard;
