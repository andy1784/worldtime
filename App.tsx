import React, { useState, useEffect, useMemo, useRef } from 'react';
import { Search, Clock, Globe, Plus, X, Calendar, Trash2, Copy, Check } from 'lucide-react';
import { CITIES, City } from './constants';
import { motion, AnimatePresence } from 'framer-motion';
import { clsx, type ClassValue } from 'clsx';
import { twMerge } from 'tailwind-merge';

function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

// Helper to get user's local timezone
const getLocalTimezone = () => {
  try {
    return Intl.DateTimeFormat().resolvedOptions().timeZone;
  } catch (e) {
    return 'UTC';
  }
};

const LOCAL_TZ = getLocalTimezone();

export default function App() {
  const [baseTime, setBaseTime] = useState(new Date());
  const [isLive, setIsLive] = useState(true);
  
  // Default cities: Local, NY, London, Tokyo
  const [selectedCities, setSelectedCities] = useState<City[]>(() => {
    const localCity = CITIES.find(c => c.timezone === LOCAL_TZ) || { name: 'Local', country: 'Current Location', timezone: LOCAL_TZ };
    const defaults = [
      localCity,
      CITIES.find(c => c.name === 'New York')!,
      CITIES.find(c => c.name === 'London')!,
      CITIES.find(c => c.name === 'Tokyo')!
    ].filter(Boolean);
    
    // Remove duplicates if local is one of the defaults
    const unique = Array.from(new Map(defaults.map(item => [item.timezone, item])).values());
    return unique;
  });

  const [searchQuery, setSearchQuery] = useState('');
  const [isSearchOpen, setIsSearchOpen] = useState(false);
  const searchInputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    if (!isLive) return;
    const timer = setInterval(() => setBaseTime(new Date()), 1000);
    return () => clearInterval(timer);
  }, [isLive]);

  // Focus search input when opened
  useEffect(() => {
    if (isSearchOpen && searchInputRef.current) {
      searchInputRef.current.focus();
    }
  }, [isSearchOpen]);

  const filteredCities = useMemo(() => {
    if (!searchQuery) return CITIES.slice(0, 10);
    const query = searchQuery.toLowerCase();
    return CITIES.filter(c => 
      c.name.toLowerCase().includes(query) || 
      c.country.toLowerCase().includes(query) ||
      c.timezone.toLowerCase().includes(query)
    ).slice(0, 10);
  }, [searchQuery]);

  const addCity = (city: City) => {
    if (!selectedCities.find(c => c.timezone === city.timezone)) {
      setSelectedCities([...selectedCities, city]);
    }
    setSearchQuery('');
    setIsSearchOpen(false);
  };

  const removeCity = (timezone: string) => {
    setSelectedCities(selectedCities.filter(c => c.timezone !== timezone));
  };

  const handleTimeChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setIsLive(false);
    const [hours, minutes] = e.target.value.split(':').map(Number);
    const newTime = new Date(baseTime);
    newTime.setHours(hours, minutes, 0, 0);
    setBaseTime(newTime);
  };

  const handleDateChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setIsLive(false);
    const [year, month, day] = e.target.value.split('-').map(Number);
    const newTime = new Date(baseTime);
    newTime.setFullYear(year, month - 1, day);
    setBaseTime(newTime);
  };

  const resetToLive = () => {
    setBaseTime(new Date());
    setIsLive(true);
  };

  return (
    <div className="min-h-screen bg-[#09090b] text-zinc-100 flex flex-col font-sans selection:bg-indigo-500/30">
      {/* Header */}
      <header className="sticky top-0 z-30 bg-[#09090b]/80 backdrop-blur-xl border-b border-white/5 px-6 py-4 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-indigo-500/10 flex items-center justify-center border border-indigo-500/20">
            <Globe className="w-5 h-5 text-indigo-400" />
          </div>
          <div>
            <h1 className="text-lg font-semibold tracking-tight">World Time Sync</h1>
            <p className="text-xs text-zinc-500 font-medium">Global Clock & Converter</p>
          </div>
        </div>

        <div className="flex items-center gap-3">
          <button
            onClick={() => setIsSearchOpen(true)}
            className="flex items-center gap-2 px-4 py-2 rounded-full bg-zinc-900 border border-white/5 hover:bg-zinc-800 transition-colors text-sm font-medium text-zinc-300"
          >
            <Plus className="w-4 h-4" />
            <span className="hidden sm:inline">Add City</span>
          </button>
        </div>
      </header>

      {/* Main Content */}
      <main className="flex-1 overflow-y-auto p-6 pb-32">
        <div className="max-w-5xl mx-auto">
          
          {/* Controls / Converter Bar */}
          <div className="mb-8 p-4 rounded-2xl bg-zinc-900/50 border border-white/5 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
            <div className="flex items-center gap-3">
              <div className={cn("px-3 py-1 rounded-full text-xs font-semibold uppercase tracking-wider flex items-center gap-1.5", 
                isLive ? "bg-emerald-500/10 text-emerald-400 border border-emerald-500/20" : "bg-amber-500/10 text-amber-400 border border-amber-500/20"
              )}>
                {isLive ? <span className="relative flex h-2 w-2"><span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span><span className="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span></span> : <Clock className="w-3 h-3" />}
                {isLive ? 'Live Time' : 'Converter Mode'}
              </div>
              {!isLive && (
                <button onClick={resetToLive} className="text-xs text-zinc-400 hover:text-white underline underline-offset-2 transition-colors">
                  Reset to Live
                </button>
              )}
            </div>

            <div className="flex items-center gap-3 w-full sm:w-auto">
              <div className="flex items-center gap-2 bg-zinc-950 border border-white/10 rounded-lg px-3 py-1.5 focus-within:border-indigo-500/50 transition-colors">
                <Calendar className="w-4 h-4 text-zinc-500" />
                <input 
                  type="date" 
                  value={baseTime.toISOString().split('T')[0]}
                  onChange={handleDateChange}
                  className="bg-transparent border-none outline-none text-sm text-zinc-200 [&::-webkit-calendar-picker-indicator]:filter-[invert(1)] [&::-webkit-calendar-picker-indicator]:opacity-50 hover:[&::-webkit-calendar-picker-indicator]:opacity-100 cursor-pointer"
                />
              </div>
              <div className="flex items-center gap-2 bg-zinc-950 border border-white/10 rounded-lg px-3 py-1.5 focus-within:border-indigo-500/50 transition-colors">
                <Clock className="w-4 h-4 text-zinc-500" />
                <input 
                  type="time" 
                  value={`${baseTime.getHours().toString().padStart(2, '0')}:${baseTime.getMinutes().toString().padStart(2, '0')}`}
                  onChange={handleTimeChange}
                  className="bg-transparent border-none outline-none text-sm text-zinc-200 [&::-webkit-calendar-picker-indicator]:filter-[invert(1)] [&::-webkit-calendar-picker-indicator]:opacity-50 hover:[&::-webkit-calendar-picker-indicator]:opacity-100 cursor-pointer"
                />
              </div>
            </div>
          </div>

          {/* Cities Grid */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            <AnimatePresence mode="popLayout">
              {selectedCities.map((city) => (
                <CityCard 
                  key={city.timezone} 
                  city={city} 
                  baseTime={baseTime} 
                  onRemove={() => removeCity(city.timezone)}
                  isLocal={city.timezone === LOCAL_TZ}
                />
              ))}
            </AnimatePresence>
            
            {/* Add New Card Button */}
            <motion.button
              layout
              onClick={() => setIsSearchOpen(true)}
              className="h-[180px] rounded-2xl border-2 border-dashed border-white/10 hover:border-white/20 hover:bg-white/5 transition-all flex flex-col items-center justify-center gap-3 text-zinc-500 hover:text-zinc-300 group"
            >
              <div className="w-12 h-12 rounded-full bg-zinc-900 flex items-center justify-center group-hover:scale-110 transition-transform">
                <Plus className="w-6 h-6" />
              </div>
              <span className="font-medium">Add City</span>
            </motion.button>
          </div>
        </div>
      </main>

      {/* Search Modal */}
      <AnimatePresence>
        {isSearchOpen && (
          <>
            <motion.div 
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              onClick={() => setIsSearchOpen(false)}
              className="fixed inset-0 bg-black/60 backdrop-blur-sm z-40"
            />
            <motion.div 
              initial={{ opacity: 0, scale: 0.95, y: 20 }}
              animate={{ opacity: 1, scale: 1, y: 0 }}
              exit={{ opacity: 0, scale: 0.95, y: 20 }}
              className="fixed top-[15%] left-1/2 -translate-x-1/2 w-full max-w-lg bg-zinc-900 border border-white/10 rounded-2xl shadow-2xl z-50 overflow-hidden flex flex-col max-h-[70vh]"
            >
              <div className="p-4 border-b border-white/10 flex items-center gap-3">
                <Search className="w-5 h-5 text-zinc-400" />
                <input
                  ref={searchInputRef}
                  type="text"
                  placeholder="Search for a city or timezone..."
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  className="flex-1 bg-transparent border-none outline-none text-zinc-100 placeholder:text-zinc-500 text-lg"
                />
                <button onClick={() => setIsSearchOpen(false)} className="p-2 hover:bg-white/5 rounded-lg text-zinc-400 hover:text-white transition-colors">
                  <X className="w-5 h-5" />
                </button>
              </div>
              <div className="overflow-y-auto p-2">
                {filteredCities.length > 0 ? (
                  filteredCities.map(city => (
                    <button
                      key={city.timezone}
                      onClick={() => addCity(city)}
                      className="w-full flex items-center justify-between p-3 rounded-xl hover:bg-white/5 transition-colors text-left group"
                    >
                      <div>
                        <div className="font-medium text-zinc-200 group-hover:text-white transition-colors">{city.name}</div>
                        <div className="text-sm text-zinc-500">{city.country} • {city.timezone}</div>
                      </div>
                      <Plus className="w-5 h-5 text-zinc-600 group-hover:text-indigo-400 transition-colors" />
                    </button>
                  ))
                ) : (
                  <div className="p-8 text-center text-zinc-500">
                    No cities found matching "{searchQuery}"
                  </div>
                )}
              </div>
            </motion.div>
          </>
        )}
      </AnimatePresence>
    </div>
  );
}

function CityCard({ city, baseTime, onRemove, isLocal }: { city: City, baseTime: Date, onRemove: () => void, isLocal: boolean }) {
  const [copied, setCopied] = useState(false);

  // Format time and date for this specific timezone
  const timeString = new Intl.DateTimeFormat('en-US', {
    timeZone: city.timezone,
    hour: 'numeric',
    minute: '2-digit',
    hour12: true,
  }).format(baseTime);

  const dateString = new Intl.DateTimeFormat('en-US', {
    timeZone: city.timezone,
    weekday: 'short',
    month: 'short',
    day: 'numeric',
  }).format(baseTime);

  const handleCopy = () => {
    navigator.clipboard.writeText(`${city.name}: ${timeString} ${dateString}`);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  // Calculate offset from local
  const getOffsetString = () => {
    if (isLocal) return 'Local Time';
    
    const parts = new Intl.DateTimeFormat('en-US', {
      timeZone: city.timezone,
      timeZoneName: 'shortOffset',
    }).formatToParts(baseTime);
    const offsetPart = parts.find(p => p.type === 'timeZoneName')?.value;
    
    const localParts = new Intl.DateTimeFormat('en-US', {
      timeZone: LOCAL_TZ,
      timeZoneName: 'shortOffset',
    }).formatToParts(baseTime);
    const localOffsetPart = localParts.find(p => p.type === 'timeZoneName')?.value;

    const parseOffset = (str: string | undefined) => {
      if (!str || str === 'GMT') return 0;
      const match = str.match(/GMT([+-])(\d+)(?::(\d+))?/);
      if (!match) return 0;
      const sign = match[1] === '-' ? -1 : 1;
      const hours = parseInt(match[2], 10);
      const mins = match[3] ? parseInt(match[3], 10) : 0;
      return sign * (hours + mins / 60);
    };

    const targetOffset = parseOffset(offsetPart);
    const localOffset = parseOffset(localOffsetPart);
    const diff = targetOffset - localOffset;

    if (diff === 0) return 'Same time';
    const sign = diff > 0 ? '+' : '';
    const hours = Math.floor(Math.abs(diff));
    const mins = Math.round((Math.abs(diff) - hours) * 60);
    const minsStr = mins > 0 ? `:${mins.toString().padStart(2, '0')}` : '';
    return `${sign}${diff > 0 ? hours : -hours}${minsStr} HRS`;
  };

  // Get timezone abbreviation (e.g., EST, GMT)
  const tzAbbr = new Intl.DateTimeFormat('en-US', {
    timeZone: city.timezone,
    timeZoneName: 'short',
  }).formatToParts(baseTime).find(p => p.type === 'timeZoneName')?.value || '';

  return (
    <motion.div
      layout
      initial={{ opacity: 0, scale: 0.9 }}
      animate={{ opacity: 1, scale: 1 }}
      exit={{ opacity: 0, scale: 0.9 }}
      className="relative group bg-zinc-900 border border-white/10 rounded-2xl p-6 overflow-hidden hover:border-white/20 transition-colors"
    >
      {/* Background Glow */}
      <div className="absolute -top-24 -right-24 w-48 h-48 bg-indigo-500/10 rounded-full blur-3xl opacity-0 group-hover:opacity-100 transition-opacity duration-500" />

      <div className="absolute top-4 right-4 flex items-center gap-2 opacity-0 group-hover:opacity-100 transition-all">
        <button 
          onClick={handleCopy}
          className="p-2 rounded-lg bg-black/20 text-zinc-500 hover:text-zinc-300 hover:bg-white/10 transition-all"
          title="Copy time"
        >
          {copied ? <Check className="w-4 h-4 text-emerald-400" /> : <Copy className="w-4 h-4" />}
        </button>
        <button 
          onClick={onRemove}
          className="p-2 rounded-lg bg-black/20 text-zinc-500 hover:text-red-400 hover:bg-red-500/10 transition-all"
          title="Remove city"
        >
          <Trash2 className="w-4 h-4" />
        </button>
      </div>

      <div className="flex flex-col h-full justify-between gap-6 relative z-10">
        <div>
          <div className="flex items-center gap-2 mb-1">
            <h2 className="text-xl font-semibold text-zinc-100">{city.name}</h2>
            {isLocal && (
              <span className="px-2 py-0.5 rounded text-[10px] font-bold uppercase tracking-wider bg-indigo-500/20 text-indigo-300">
                Home
              </span>
            )}
          </div>
          <p className="text-sm text-zinc-500">{city.country}</p>
        </div>

        <div>
          <div className="flex items-baseline gap-2 mb-1">
            <span className="text-4xl font-bold tracking-tight text-white font-mono">
              {timeString.split(' ')[0]}
            </span>
            <span className="text-lg font-medium text-zinc-400">
              {timeString.split(' ')[1]}
            </span>
          </div>
          <div className="flex items-center justify-between text-sm font-medium">
            <span className="text-zinc-400">{dateString}</span>
            <div className="flex items-center gap-2">
              <span className="text-zinc-500">{tzAbbr}</span>
              <span className="w-1 h-1 rounded-full bg-zinc-700" />
              <span className={cn(
                "text-xs",
                isLocal ? "text-indigo-400" : "text-zinc-500"
              )}>
                {getOffsetString()}
              </span>
            </div>
          </div>
        </div>
      </div>
    </motion.div>
  );
}
