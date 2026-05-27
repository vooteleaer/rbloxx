const TILE_SIZE = 256;

export interface TileInfo {
  x: number;  // tile column
  y: number;  // tile row
  px: number; // pixel offset within tile (0–255), longitude axis
  py: number; // pixel offset within tile (0–255), latitude axis
}

export function latLonToTile(lat: number, lon: number, zoom: number): TileInfo {
  const n = Math.pow(2, zoom);
  const x = Math.floor((lon + 180) / 360 * n);
  const latRad = (lat * Math.PI) / 180;
  const y = Math.floor((1 - Math.log(Math.tan(latRad) + 1 / Math.cos(latRad)) / Math.PI) / 2 * n);

  const xFrac = (lon + 180) / 360 * n - x;
  const yFrac = (1 - Math.log(Math.tan(latRad) + 1 / Math.cos(latRad)) / Math.PI) / 2 * n - y;

  return {
    x: Math.max(0, Math.min(n - 1, x)),
    y: Math.max(0, Math.min(n - 1, y)),
    px: Math.round(xFrac * TILE_SIZE),
    py: Math.round(yFrac * TILE_SIZE),
  };
}

export { TILE_SIZE };
