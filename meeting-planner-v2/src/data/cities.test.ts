import { describe, it, expect } from 'vitest';
import { CITIES, searchCities, getCityById, getCitiesByIds, filterByCountry, getCountries, getTimezones } from './cities';

describe('cities data module', () => {
  it('should load 682 cities', () => {
    expect(CITIES.length).toBe(682);
  });

  it('should have correct structure for each city', () => {
    const city = CITIES[0];
    expect(city).toHaveProperty('id');
    expect(city).toHaveProperty('name');
    expect(city).toHaveProperty('country');
    expect(city).toHaveProperty('timezone');
    expect(typeof city.id).toBe('string');
    expect(typeof city.name).toBe('string');
    expect(typeof city.country).toBe('string');
    expect(typeof city.timezone).toBe('string');
  });

  describe('searchCities', () => {
    it('returns empty for query < 2 chars', () => {
      expect(searchCities('')).toEqual([]);
      expect(searchCities('a')).toEqual([]);
    });

    it('finds cities by name', () => {
      const results = searchCities('new york');
      expect(results.length).toBeGreaterThan(0);
      expect(results.some(c => c.name === 'New York')).toBe(true);
    });

    it('finds cities by country', () => {
      const results = searchCities('canada');
      expect(results.length).toBeGreaterThan(0);
      expect(results.every(c => c.country === 'Canada')).toBe(true);
    });

    it('finds cities by timezone', () => {
      const results = searchCities('america/new_york');
      expect(results.length).toBeGreaterThan(0);
      expect(results.every(c => c.timezone === 'America/New_York')).toBe(true);
    });

    it('excludes specified IDs', () => {
      const results = searchCities('new', ['nyc']);
      expect(results.some(c => c.id === 'nyc')).toBe(false);
    });

    it('limits to 10 results', () => {
      const results = searchCities('a');
      expect(results.length).toBeLessThanOrEqual(10);
    });
  });

  describe('getCityById', () => {
    it('returns city for valid ID', () => {
      const city = getCityById('nyc');
      expect(city).toBeDefined();
      expect(city?.name).toBe('New York');
    });

    it('returns undefined for invalid ID', () => {
      expect(getCityById('invalid')).toBeUndefined();
    });
  });

  describe('getCitiesByIds', () => {
    it('returns cities in same order as IDs', () => {
      const cities = getCitiesByIds(['lax', 'nyc', 'chi']);
      expect(cities.map(c => c.id)).toEqual(['lax', 'nyc', 'chi']);
    });

    it('skips invalid IDs', () => {
      const cities = getCitiesByIds(['nyc', 'invalid', 'lax']);
      expect(cities.map(c => c.id)).toEqual(['nyc', 'lax']);
    });
  });

  describe('filterByCountry', () => {
    it('returns cities for country', () => {
      const results = filterByCountry('Canada');
      expect(results.length).toBeGreaterThan(0);
      expect(results.every(c => c.country === 'Canada')).toBe(true);
    });

    it('returns empty for non-existent country', () => {
      expect(filterByCountry('Atlantis')).toEqual([]);
    });
  });

  describe('getCountries', () => {
    it('returns sorted unique countries', () => {
      const countries = getCountries();
      expect(countries.length).toBeGreaterThan(0);
      expect(countries).toEqual([...countries].sort());
      expect(new Set(countries).size).toBe(countries.length);
    });
  });

  describe('getTimezones', () => {
    it('returns sorted unique timezones', () => {
      const timezones = getTimezones();
      expect(timezones.length).toBeGreaterThan(0);
      expect(timezones).toEqual([...timezones].sort());
      expect(new Set(timezones).size).toBe(timezones.length);
    });
  });
});