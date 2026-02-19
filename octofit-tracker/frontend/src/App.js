import './App.css';
import { Routes, Route, NavLink } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

const navItems = [
  { to: '/users',       label: 'Users' },
  { to: '/teams',       label: 'Teams' },
  { to: '/activities',  label: 'Activities' },
  { to: '/leaderboard', label: 'Leaderboard' },
  { to: '/workouts',    label: 'Workouts' },
];

const featureCards = [
  { icon: '👤', title: 'Users',       desc: 'Manage member profiles and accounts.',            to: '/users' },
  { icon: '🏆', title: 'Leaderboard', desc: 'See who leads the fitness challenge.',            to: '/leaderboard' },
  { icon: '🏃', title: 'Activities',  desc: 'Log and review individual activity sessions.',    to: '/activities' },
  { icon: '👥', title: 'Teams',       desc: 'Create and manage your fitness teams.',           to: '/teams' },
  { icon: '💪', title: 'Workouts',    desc: 'Browse personalised workout suggestions.',        to: '/workouts' },
];

function App() {
  return (
    <div className="App">
      {/* ── Navbar ── */}
      <nav className="navbar navbar-expand-lg navbar-dark octofit-navbar">
        <div className="container">
          <NavLink className="navbar-brand" to="/">
            <img
              src={`${process.env.PUBLIC_URL}/octofit-logo.png`}
              alt=""
              onError={(e) => { e.target.style.display = 'none'; }}
            />
            OctoFit Tracker
          </NavLink>
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav ms-auto">
              {navItems.map(({ to, label }) => (
                <li className="nav-item" key={to}>
                  <NavLink
                    className={({ isActive }) =>
                      'nav-link' + (isActive ? ' active' : '')
                    }
                    to={to}
                  >
                    {label}
                  </NavLink>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </nav>

      {/* ── Routes ── */}
      <Routes>
        <Route
          path="/"
          element={
            <>
              {/* Hero */}
              <div className="octofit-hero text-center">
                <div className="container">
                  <h1 className="display-4 fw-bold">Welcome to OctoFit Tracker</h1>
                  <p className="lead mt-3">
                    Track your fitness activities, compete with teammates, and crush your goals.
                  </p>
                  <NavLink className="btn btn-outline-light btn-lg mt-3" to="/activities">
                    Get Started
                  </NavLink>
                </div>
              </div>

              {/* Feature cards */}
              <div className="container pb-5">
                <h2 className="h4 fw-semibold text-center mb-4 text-white">Explore OctoFit</h2>
                <div className="row g-4 justify-content-center">
                  {featureCards.map(({ icon, title, desc, to }) => (
                    <div className="col-12 col-sm-6 col-lg-4" key={to}>
                      <NavLink to={to} style={{ textDecoration: 'none' }}>
                        <div className="card feature-card h-100 shadow-sm">
                          <div className="card-body text-center">
                            <div className="feature-icon">{icon}</div>
                            <h5 className="card-title fw-semibold">{title}</h5>
                            <p className="card-text text-muted">{desc}</p>
                          </div>
                        </div>
                      </NavLink>
                    </div>
                  ))}
                </div>
              </div>
            </>
          }
        />
        <Route path="/users"       element={<Users />} />
        <Route path="/teams"       element={<Teams />} />
        <Route path="/activities"  element={<Activities />} />
        <Route path="/leaderboard" element={<Leaderboard />} />
        <Route path="/workouts"    element={<Workouts />} />
      </Routes>

      {/* ── Footer ── */}
      <footer className="octofit-footer">
        © {new Date().getFullYear()} OctoFit Tracker — Built with React &amp; Django
      </footer>
    </div>
  );
}

export default App;
