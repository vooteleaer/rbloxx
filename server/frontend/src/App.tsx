import { BrowserRouter, Routes, Route, NavLink } from "react-router-dom";
import NodesView from "./pages/NodesView";
import TopologyMap from "./pages/TopologyMap";

export default function App() {
  return (
    <BrowserRouter>
      <div className="min-h-screen bg-gray-50">
        <header className="bg-white border-b border-gray-200 px-6 py-3 flex items-center gap-6">
          <span className="text-lg font-bold tracking-tight select-none"><span className="text-red-600 italic">R</span><span className="text-gray-900 italic">Bloxx</span></span>
          <nav className="flex items-center gap-4 text-sm">
            <NavLink
              to="/"
              end
              className={({ isActive }) =>
                isActive ? "text-blue-600 font-medium" : "text-gray-500 hover:text-gray-900"
              }
            >
              Nodes
            </NavLink>
            <NavLink
              to="/topology"
              className={({ isActive }) =>
                isActive ? "text-blue-600 font-medium" : "text-gray-500 hover:text-gray-900"
              }
            >
              Topology
            </NavLink>
          </nav>
        </header>
        <main>
          <Routes>
            <Route path="/" element={<NodesView />} />
            <Route path="/topology" element={<TopologyMap />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}
