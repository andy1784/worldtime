export interface City {
  id: string;
  name: string;
  country: string;
  timezone: string;
}

// Load cities from JSON (bundled at build time)
import citiesJson from './cities.json' with { type: 'json' };

export const CITIES: City[] = citiesJson as City[];

/**
 * Search cities by query string (name, country, or timezone)
 * Returns up to 10 results, excluding already selected cities
 */
export function searchCities(query: string, excludeIds: string[] = []): City[] {
  const q = query.toLowerCase().trim();
  if (q.length < 2) return [];

  const excludeSet = new Set(excludeIds);
  return CITIES.filter(city =>
    !excludeSet.has(city.id) &&
    (city.name.toLowerCase().includes(q) ||
     city.country.toLowerCase().includes(q) ||
     city.timezone.toLowerCase().includes(q))
  ).slice(0, 10);
}

/**
 * Get a city by its ID
 */
export function getCityById(id: string): City | undefined {
  return CITIES.find(city => city.id === id);
}

/**
 * Get multiple cities by their IDs, preserving input order
 */
export function getCitiesByIds(ids: string[]): City[] {
  const cityMap = new Map(CITIES.map(city => [city.id, city]));
  return ids.map(id => cityMap.get(id)).filter((city): city is City => city !== undefined);
}

/**
 * Filter cities by country
 */
export function filterByCountry(country: string): City[] {
  const q = country.toLowerCase().trim();
  if (!q) return [];
  return CITIES.filter(city => city.country.toLowerCase().includes(q));
}

/**
 * Get all unique countries
 */
export function getCountries(): string[] {
  const countries = new Set(CITIES.map(city => city.country));
  return Array.from(countries).sort();
}

/**
 * Get all unique timezones
 */
export function getTimezones(): string[] {
  const timezones = new Set(CITIES.map(city => city.timezone));
  return Array.from(timezones).sort();
}