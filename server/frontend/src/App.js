import { jsx as _jsx, jsxs as _jsxs } from "react/jsx-runtime";
import { BrowserRouter, Routes, Route, NavLink } from "react-router-dom";
import NodesView from "./pages/NodesView";
import TopologyMap from "./pages/TopologyMap";
export default function App() {
    return (_jsx(BrowserRouter, { children: _jsxs("div", { className: "min-h-screen bg-gray-50", children: [_jsxs("header", { className: "bg-white border-b border-gray-200 px-6 py-3 flex items-center gap-6", children: [_jsxs("span", { className: "text-lg font-bold tracking-tight select-none", children: [_jsx("span", { className: "text-red-600 italic", children: "R" }), _jsx("span", { className: "text-gray-900 italic", children: "Bloxx" })] }), _jsxs("nav", { className: "flex items-center gap-4 text-sm", children: [_jsx(NavLink, { to: "/", end: true, className: ({ isActive }) => isActive ? "text-blue-600 font-medium" : "text-gray-500 hover:text-gray-900", children: "Nodes" }), _jsx(NavLink, { to: "/topology", className: ({ isActive }) => isActive ? "text-blue-600 font-medium" : "text-gray-500 hover:text-gray-900", children: "Topology" })] })] }), _jsx("main", { children: _jsxs(Routes, { children: [_jsx(Route, { path: "/", element: _jsx(NodesView, {}) }), _jsx(Route, { path: "/topology", element: _jsx(TopologyMap, {}) })] }) })] }) }));
}
