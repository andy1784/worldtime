import React from 'react';
import { CITIES } from '../data/cities';

interface MeetingGridProps {}

export default function MeetingGrid({}: MeetingGridProps) {
  return (
    <div style={{ display: 'none' }}>
      {/* React island placeholder - interactive version coming in #26 */}
      <p>Meeting Planner v2 - Interactive grid will hydrate here</p>
      <p>Cities loaded: {CITIES.length}</p>
    </div>
  );
}