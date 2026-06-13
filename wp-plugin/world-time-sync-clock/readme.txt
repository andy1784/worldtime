=== World Time Sync Clock ===
Contributors: andy1784
Tags: clock, world clock, timezone, time, widget, shortcode
Requires at least: 5.0
Tested up to: 6.5
Requires PHP: 7.2
Stable tag: 1.0.0
License: GPLv2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html

Add a beautiful, real-time world clock to your WordPress site. Supports 682 cities, dark/light themes, and multiple sizes.

== Description ==

World Time Sync Clock is a free WordPress plugin that lets you display a real-time clock for any city worldwide. Perfect for global businesses, remote teams, travel sites, and anyone who works across time zones.

**Features:**

* Real-time clock updates every second
* 682 cities across all time zones
* Dark and light themes
* Three sizes: small, medium, large
* Optional date display
* Shortcode support: `[world_time_clock]`
* Widget support (Appearance → Widgets)
* Gutenberg block editor support
* Lightweight - loads via iframe, no heavy JS
* No API key required
* Free forever

**Shortcode Examples:**

Basic usage:
`[world_time_clock]`

Custom timezone:
`[world_time_clock timezone="Asia/Tokyo"]`

Full customization:
`[world_time_clock timezone="Europe/London" theme="light" size="large" show_date="true"]`

**Parameters:**

* `timezone` - IANA timezone (default: America/New_York)
* `theme` - "dark" or "light" (default: dark)
* `size` - "small", "medium", or "large" (default: medium)
* `show_date` - "true" or "false" (default: true)

**About World Time Sync:**

World Time Sync is a free suite of time tools for global teams. Visit [worldtimessync.com](https://worldtimessync.com) for the web version, meeting planner, and more.

== Installation ==

1. Upload the `world-time-sync-clock` folder to `/wp-content/plugins/`
2. Activate the plugin through the 'Plugins' menu in WordPress
3. Go to Settings → World Time Clock to configure defaults
4. Use the shortcode `[world_time_clock]` in any post or page
5. Or add the "World Time Clock" widget in Appearance → Widgets
6. Or use the "World Time Clock" block in the block editor

== Frequently Asked Questions ==

= Is this plugin free? =

Yes, completely free. No premium tier, no API key, no signup required.

= How many cities are supported? =

682 cities across all time zones worldwide.

= Does it work with the block editor? =

Yes! Search for "World Time Clock" in the block inserter.

= Can I customize the appearance? =

Yes - dark/light theme, three sizes, and optional date display.

== Changelog ==

= 1.0.0 =
* Initial release
* Shortcode, widget, and block editor support
* 682 cities, dark/light themes, 3 sizes
* Settings page for defaults
