import React, { useState, useEffect } from 'react';

function Users() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;

  useEffect(() => {
    console.log('Users: fetching from', apiUrl);
    fetch(apiUrl)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        console.log('Users: fetched data', data);
        // Support both paginated (.results) and plain array responses
        const items = Array.isArray(data) ? data : data.results || [];
        setUsers(items);
        setLoading(false);
      })
      .catch((err) => {
        console.error('Users: fetch error', err);
        setError(err.message);
        setLoading(false);
      });
  }, [apiUrl]);

  if (loading) {
    return (
      <div className="container octofit-loading">
        <div className="spinner-border text-info me-3" role="status" aria-hidden="true"></div>
        <span className="fs-5">Loading users...</span>
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
          <h2 className="mb-0">👤 Users</h2>
          <span className="badge bg-secondary">{users.length} users</span>
        </div>
        <div className="card-body p-0">
          <div className="table-responsive">
            <table className="table table-striped table-bordered table-hover octofit-table mb-0">
              <thead>
                <tr>
                  <th scope="col">#</th>
                  <th scope="col">Username</th>
                  <th scope="col">Email</th>
                  <th scope="col">Team</th>
                </tr>
              </thead>
              <tbody>
                {users.length === 0 ? (
                  <tr>
                    <td colSpan="4" className="text-center text-muted py-4">No users found.</td>
                  </tr>
                ) : (
                  users.map((user, idx) => (
                    <tr key={user._id || user.id}>
                      <td className="text-muted">{idx + 1}</td>
                      <td className="fw-semibold">{user.username}</td>
                      <td>
                        <a href={`mailto:${user.email}`} className="link-primary">{user.email}</a>
                      </td>
                      <td>
                        {user.team ? (
                          <span className={`badge ${user.team.toLowerCase().includes('marvel') ? 'bg-danger' : 'bg-primary'}`}>
                            {user.team}
                          </span>
                        ) : (
                          <span className="text-muted">—</span>
                        )}
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

export default Users;
