<?php
/**
 * Plugin Name: World Time Sync Clock
 * Plugin URI: https://worldtimessync.com/wordpress
 * Description: Add a beautiful, real-time world clock to your WordPress site. Supports 682 cities, dark/light themes, and multiple sizes. No API key required.
 * Version: 1.0.0
 * Author: World Time Sync
 * Author URI: https://worldtimessync.com
 * License: GPL v2 or later
 * License URI: https://www.gnu.org/licenses/gpl-2.0.html
 * Text Domain: world-time-sync
 * Domain Path: /languages
 */

// Prevent direct access
if (!defined('ABSPATH')) {
    exit;
}

// Plugin constants
define('WTS_VERSION', '1.0.0');
define('WTS_PLUGIN_DIR', plugin_dir_path(__FILE__));
define('WTS_PLUGIN_URL', plugin_dir_url(__FILE__));
define('WTS_PLUGIN_BASENAME', plugin_basename(__FILE__));

/**
 * Main plugin class
 */
class World_Time_Sync_Clock {

    private static $instance = null;

    public static function get_instance() {
        if (null === self::$instance) {
            self::$instance = new self();
        }
        return self::$instance;
    }

    private function __construct() {
        add_action('init', array($this, 'init'));
        add_action('widgets_init', array($this, 'register_widget'));
        add_action('admin_menu', array($this, 'add_admin_menu'));
        add_action('admin_init', array($this, 'register_settings'));
        add_action('enqueue_block_editor_assets', array($this, 'enqueue_block_assets'));
        add_action('wp_enqueue_scripts', array($this, 'enqueue_frontend_styles'));
        
        // Register shortcode
        add_shortcode('world_time_clock', array($this, 'render_shortcode'));
        add_shortcode('wtc_clock', array($this, 'render_shortcode'));
    }

    /**
     * Initialize plugin
     */
    public function init() {
        load_plugin_textdomain('world-time-sync', false, dirname(WTS_PLUGIN_BASENAME) . '/languages');
    }

    /**
     * Enqueue frontend styles
     */
    public function enqueue_frontend_styles() {
        // Only enqueue if shortcode or widget is present
        global $post;
        if (is_a($post, 'WP_Post') && (has_shortcode($post->post_content, 'world_time_clock') || has_shortcode($post->post_content, 'wtc_clock'))) {
            // Styles are inline in the widget output
        }
    }

    /**
     * Register the widget
     */
    public function register_widget() {
        register_widget('WTS_Clock_Widget');
    }

    /**
     * Add admin menu
     */
    public function add_admin_menu() {
        add_options_page(
            __('World Time Sync Clock', 'world-time-sync'),
            __('World Time Clock', 'world-time-sync'),
            'manage_options',
            'world-time-sync',
            array($this, 'render_settings_page')
        );
    }

    /**
     * Register settings
     */
    public function register_settings() {
        register_setting('wts_settings_group', 'wts_default_timezone', array(
            'type' => 'string',
            'default' => 'America/New_York',
            'sanitize_callback' => 'sanitize_text_field',
        ));
        register_setting('wts_settings_group', 'wts_default_theme', array(
            'type' => 'string',
            'default' => 'dark',
            'sanitize_callback' => 'sanitize_text_field',
        ));
        register_setting('wts_settings_group', 'wts_default_size', array(
            'type' => 'string',
            'default' => 'medium',
            'sanitize_callback' => 'sanitize_text_field',
        ));
        register_setting('wts_settings_group', 'wts_default_show_date', array(
            'type' => 'string',
            'default' => 'true',
            'sanitize_callback' => 'sanitize_text_field',
        ));
    }

    /**
     * Render settings page
     */
    public function render_settings_page() {
        if (!current_user_can('manage_options')) {
            return;
        }
        ?>
        <div class="wrap">
            <h1><?php echo esc_html(get_admin_page_title()); ?></h1>
            
            <div style="max-width:800px;">
                <div style="background:#fff;border:1px solid #ccd0d4;border-radius:8px;padding:24px;margin-bottom:24px;">
                    <h2 style="margin-top:0;"><?php _e('Default Settings', 'world-time-sync'); ?></h2>
                    <p style="color:#666;"><?php _e('Configure default values for the World Time Clock. These can be overridden per shortcode or widget.', 'world-time-sync'); ?></p>
                    
                    <form method="post" action="options.php">
                        <?php settings_fields('wts_settings_group'); ?>
                        <table class="form-table">
                            <tr>
                                <th scope="row"><label for="wts_default_timezone"><?php _e('Default Timezone', 'world-time-sync'); ?></label></th>
                                <td>
                                    <select name="wts_default_timezone" id="wts_default_timezone" style="min-width:250px;">
                                        <?php echo $this->get_timezone_options(get_option('wts_default_timezone', 'America/New_York')); ?>
                                    </select>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row"><label for="wts_default_theme"><?php _e('Default Theme', 'world-time-sync'); ?></label></th>
                                <td>
                                    <select name="wts_default_theme" id="wts_default_theme">
                                        <option value="dark" <?php selected(get_option('wts_default_theme', 'dark'), 'dark'); ?>><?php _e('Dark', 'world-time-sync'); ?></option>
                                        <option value="light" <?php selected(get_option('wts_default_theme', 'dark'), 'light'); ?>><?php _e('Light', 'world-time-sync'); ?></option>
                                    </select>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row"><label for="wts_default_size"><?php _e('Default Size', 'world-time-sync'); ?></label></th>
                                <td>
                                    <select name="wts_default_size" id="wts_default_size">
                                        <option value="small" <?php selected(get_option('wts_default_size', 'medium'), 'small'); ?>><?php _e('Small (220×120)', 'world-time-sync'); ?></option>
                                        <option value="medium" <?php selected(get_option('wts_default_size', 'medium'), 'medium'); ?>><?php _e('Medium (300×160)', 'world-time-sync'); ?></option>
                                        <option value="large" <?php selected(get_option('wts_default_size', 'medium'), 'large'); ?>><?php _e('Large (420×220)', 'world-time-sync'); ?></option>
                                    </select>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row"><label for="wts_default_show_date"><?php _e('Show Date', 'world-time-sync'); ?></label></th>
                                <td>
                                    <select name="wts_default_show_date" id="wts_default_show_date">
                                        <option value="true" <?php selected(get_option('wts_default_show_date', 'true'), 'true'); ?>><?php _e('Yes', 'world-time-sync'); ?></option>
                                        <option value="false" <?php selected(get_option('wts_default_show_date', 'true'), 'false'); ?>><?php _e('No', 'world-time-sync'); ?></option>
                                    </select>
                                </td>
                            </tr>
                        </table>
                        <?php submit_button(); ?>
                    </form>
                </div>
                
                <div style="background:#fff;border:1px solid #ccd0d4;border-radius:8px;padding:24px;margin-bottom:24px;">
                    <h2 style="margin-top:0;"><?php _e('How to Use', 'world-time-sync'); ?></h2>
                    
                    <h3><?php _e('Shortcode', 'world-time-sync'); ?></h3>
                    <p><?php _e('Add the clock to any post or page:', 'world-time-sync'); ?></p>
                    <code style="display:block;padding:12px;background:#f6f7f7;border-radius:4px;margin:8px 0;">[world_time_clock timezone="America/New_York" theme="dark" size="medium"]</code>
                    
                    <h4><?php _e('Shortcode Parameters:', 'world-time-sync'); ?></h4>
                    <ul style="list-style:disc;margin-left:20px;">
                        <li><code>timezone</code> - <?php _e('IANA timezone (e.g., Europe/London, Asia/Tokyo)', 'world-time-sync'); ?></li>
                        <li><code>theme</code> - <?php _e('"dark" or "light"', 'world-time-sync'); ?></li>
                        <li><code>size</code> - <?php _e('"small", "medium", or "large"', 'world-time-sync'); ?></li>
                        <li><code>show_date</code> - <?php _e('"true" or "false"', 'world-time-sync'); ?></li>
                    </ul>
                    
                    <h3><?php _e('Widget', 'world-time-sync'); ?></h3>
                    <p><?php _e('Go to Appearance → Widgets and add "World Time Clock" to any widget area.', 'world-time-sync'); ?></p>
                    
                    <h3><?php _e('Block Editor (Gutenberg)', 'world-time-sync'); ?></h3>
                    <p><?php _e('Search for "World Time Clock" in the block inserter.', 'world-time-sync'); ?></p>
                </div>
                
                <div style="background:#f0f6fc;border:1px solid #c3d9ed;border-radius:8px;padding:24px;">
                    <h2 style="margin-top:0;"><?php _e('About World Time Sync', 'world-time-sync'); ?></h2>
                    <p><?php _e('World Time Sync is a free suite of time tools for global teams. This plugin embeds a real-time clock showing the time in any of 682 cities worldwide.', 'world-time-sync'); ?></p>
                    <p>
                        <a href="https://worldtimessync.com" target="_blank" rel="noopener" class="button button-secondary"><?php _e('Visit Website', 'world-time-sync'); ?></a>
                        <a href="https://worldtimessync.com/meeting-planner.html" target="_blank" rel="noopener" class="button button-secondary"><?php _e('Meeting Planner', 'world-time-sync'); ?></a>
                        <a href="https://worldtimessync.com/earth-clock.html" target="_blank" rel="noopener" class="button button-secondary"><?php _e('Earth Clock', 'world-time-sync'); ?></a>
                    </p>
                </div>
            </div>
        </div>
        <?php
    }

    /**
     * Get timezone options HTML
     */
    private function get_timezone_options($selected = '') {
        $zones = array(
            'America/New_York' => 'New York (Eastern)',
            'America/Chicago' => 'Chicago (Central)',
            'America/Denver' => 'Denver (Mountain)',
            'America/Phoenix' => 'Phoenix (MST)',
            'America/Los_Angeles' => 'Los Angeles (Pacific)',
            'America/Anchorage' => 'Anchorage (Alaska)',
            'America/Toronto' => 'Toronto',
            'America/Vancouver' => 'Vancouver',
            'America/Mexico_City' => 'Mexico City',
            'America/Sao_Paulo' => 'São Paulo',
            'America/Buenos_Aires' => 'Buenos Aires',
            'America/Bogota' => 'Bogotá',
            'America/Lima' => 'Lima',
            'America/Santiago' => 'Santiago',
            'Europe/London' => 'London (GMT)',
            'Europe/Paris' => 'Paris (CET)',
            'Europe/Berlin' => 'Berlin (CET)',
            'Europe/Rome' => 'Rome',
            'Europe/Madrid' => 'Madrid',
            'Europe/Amsterdam' => 'Amsterdam',
            'Europe/Moscow' => 'Moscow',
            'Europe/Istanbul' => 'Istanbul',
            'Europe/Zurich' => 'Zurich',
            'Asia/Dubai' => 'Dubai',
            'Asia/Kolkata' => 'Mumbai (IST)',
            'Asia/Dhaka' => 'Dhaka',
            'Asia/Bangkok' => 'Bangkok',
            'Asia/Singapore' => 'Singapore',
            'Asia/Shanghai' => 'Shanghai',
            'Asia/Hong_Kong' => 'Hong Kong',
            'Asia/Tokyo' => 'Tokyo',
            'Asia/Seoul' => 'Seoul',
            'Asia/Jakarta' => 'Jakarta',
            'Asia/Manila' => 'Manila',
            'Asia/Karachi' => 'Karachi',
            'Asia/Riyadh' => 'Riyadh',
            'Asia/Tehran' => 'Tehran',
            'Australia/Sydney' => 'Sydney',
            'Australia/Melbourne' => 'Melbourne',
            'Australia/Perth' => 'Perth',
            'Australia/Brisbane' => 'Brisbane',
            'Pacific/Auckland' => 'Auckland',
            'Pacific/Honolulu' => 'Honolulu',
            'Africa/Cairo' => 'Cairo',
            'Africa/Lagos' => 'Lagos',
            'Africa/Johannesburg' => 'Johannesburg',
            'Africa/Nairobi' => 'Nairobi',
        );
        
        $html = '';
        foreach ($zones as $tz => $label) {
            $sel = selected($selected, $tz, false);
            $html .= '<option value="' . esc_attr($tz) . '"' . $sel . '>' . esc_html($label) . '</option>';
        }
        return $html;
    }

    /**
     * Render the clock HTML
     */
    public function render_clock($atts = array()) {
        $defaults = array(
            'timezone' => get_option('wts_default_timezone', 'America/New_York'),
            'theme' => get_option('wts_default_theme', 'dark'),
            'size' => get_option('wts_default_size', 'medium'),
            'show_date' => get_option('wts_default_show_date', 'true'),
        );
        
        $atts = shortcode_atts($defaults, $atts, 'world_time_clock');
        
        $tz = sanitize_text_field($atts['timezone']);
        $theme = sanitize_text_field($atts['theme']);
        $size = sanitize_text_field($atts['size']);
        $show_date = sanitize_text_field($atts['show_date']);
        
        // Validate
        if (!in_array($theme, array('dark', 'light'))) $theme = 'dark';
        if (!in_array($size, array('small', 'medium', 'large'))) $size = 'medium';
        
        $params = array(
            'tz' => $tz,
            'theme' => $theme,
            'size' => $size,
            'date' => $show_date === 'false' ? '0' : '1',
        );
        
        $embed_url = 'https://worldtimessync.com/widget-embed.html?' . http_build_query($params);
        
        $size_dims = array(
            'small' => array('width' => '220', 'height' => '120'),
            'medium' => array('width' => '300', 'height' => '160'),
            'large' => array('width' => '420', 'height' => '220'),
        );
        $dims = $size_dims[$size];
        
        $city_slug = strtolower(preg_replace('/[^a-z0-9]+/', '-', $tz));
        $city_slug = trim($city_slug, '-');
        $link_url = 'https://worldtimessync.com/time/' . $city_slug . '.html';
        
        ob_start();
        ?>
        <div class="wts-clock-wrapper" style="display:inline-block;text-align:center;">
            <iframe 
                src="<?php echo esc_url($embed_url); ?>"
                width="<?php echo esc_attr($dims['width']); ?>"
                height="<?php echo esc_attr($dims['height']); ?>"
                frameborder="0"
                scrolling="no"
                style="border:none;border-radius:12px;overflow:hidden;"
                title="<?php esc_attr_e('World Time Clock', 'world-time-sync'); ?>"
                loading="lazy">
            </iframe>
            <br>
            <a href="<?php echo esc_url($link_url); ?>" 
               target="_blank" 
               rel="noopener noreferrer"
               style="display:inline-block;margin-top:4px;font-size:11px;color:rgba(128,128,128,0.6);text-decoration:none;font-family:system-ui,-apple-system,sans-serif;">
                <?php esc_html_e('World Time Sync', 'world-time-sync'); ?>
            </a>
        </div>
        <?php
        return ob_get_clean();
    }

    /**
     * Shortcode handler
     */
    public function render_shortcode($atts) {
        return $this->render_clock($atts);
    }

    /**
     * Enqueue block editor assets
     */
    public function enqueue_block_assets() {
        wp_enqueue_script(
            'wts-block-editor',
            WTS_PLUGIN_URL . 'assets/block-editor.js',
            array('wp-blocks', 'wp-element', 'wp-editor', 'wp-components', 'wp-i18n'),
            WTS_VERSION,
            true
        );
        
        wp_localize_script('wts-block-editor', 'wtsBlockData', array(
            'timezoneOptions' => $this->get_timezone_options_array(),
            'defaultTimezone' => get_option('wts_default_timezone', 'America/New_York'),
            'defaultTheme' => get_option('wts_default_theme', 'dark'),
            'defaultSize' => get_option('wts_default_size', 'medium'),
            'previewUrl' => 'https://worldtimessync.com/widget-embed.html',
        ));
        
        wp_enqueue_style(
            'wts-block-editor-style',
            WTS_PLUGIN_URL . 'assets/block-editor.css',
            array(),
            WTS_VERSION
        );
    }

    /**
     * Get timezone options as array for block editor
     */
    private function get_timezone_options_array() {
        return array(
            array('value' => 'America/New_York', 'label' => 'New York (Eastern)'),
            array('value' => 'America/Chicago', 'label' => 'Chicago (Central)'),
            array('value' => 'America/Denver', 'label' => 'Denver (Mountain)'),
            array('value' => 'America/Los_Angeles', 'label' => 'Los Angeles (Pacific)'),
            array('value' => 'America/Toronto', 'label' => 'Toronto'),
            array('value' => 'America/Sao_Paulo', 'label' => 'São Paulo'),
            array('value' => 'America/Mexico_City', 'label' => 'Mexico City'),
            array('value' => 'Europe/London', 'label' => 'London (GMT)'),
            array('value' => 'Europe/Paris', 'label' => 'Paris (CET)'),
            array('value' => 'Europe/Berlin', 'label' => 'Berlin (CET)'),
            array('value' => 'Europe/Madrid', 'label' => 'Madrid'),
            array('value' => 'Europe/Moscow', 'label' => 'Moscow'),
            array('value' => 'Europe/Istanbul', 'label' => 'Istanbul'),
            array('value' => 'Asia/Dubai', 'label' => 'Dubai'),
            array('value' => 'Asia/Kolkata', 'label' => 'Mumbai (IST)'),
            array('value' => 'Asia/Singapore', 'label' => 'Singapore'),
            array('value' => 'Asia/Shanghai', 'label' => 'Shanghai'),
            array('value' => 'Asia/Hong_Kong', 'label' => 'Hong Kong'),
            array('value' => 'Asia/Tokyo', 'label' => 'Tokyo'),
            array('value' => 'Asia/Seoul', 'label' => 'Seoul'),
            array('value' => 'Asia/Bangkok', 'label' => 'Bangkok'),
            array('value' => 'Asia/Jakarta', 'label' => 'Jakarta'),
            array('value' => 'Australia/Sydney', 'label' => 'Sydney'),
            array('value' => 'Australia/Melbourne', 'label' => 'Melbourne'),
            array('value' => 'Pacific/Auckland', 'label' => 'Auckland'),
            array('value' => 'Pacific/Honolulu', 'label' => 'Honolulu'),
            array('value' => 'Africa/Cairo', 'label' => 'Cairo'),
            array('value' => 'Africa/Lagos', 'label' => 'Lagos'),
            array('value' => 'Africa/Johannesburg', 'label' => 'Johannesburg'),
        );
    }

    /**
     * Plugin activation
     */
    public static function activate() {
        // Set defaults
        if (false === get_option('wts_default_timezone')) {
            update_option('wts_default_timezone', 'America/New_York');
        }
        if (false === get_option('wts_default_theme')) {
            update_option('wts_default_theme', 'dark');
        }
        if (false === get_option('wts_default_size')) {
            update_option('wts_default_size', 'medium');
        }
        if (false === get_option('wts_default_show_date')) {
            update_option('wts_default_show_date', 'true');
        }
    }

    /**
     * Plugin deactivation
     */
    public static function deactivate() {
        // Clean up if needed
    }
}

// Initialize
World_Time_Sync_Clock::get_instance();

// Activation/Deactivation hooks
register_activation_hook(__FILE__, array('World_Time_Sync_Clock', 'activate'));
register_deactivation_hook(__FILE__, array('World_Time_Sync_Clock', 'deactivate'));

/**
 * WP_Widget class for the clock
 */
class WTS_Clock_Widget extends WP_Widget {

    public function __construct() {
        parent::__construct(
            'wts_clock_widget',
            __('World Time Clock', 'world-time-sync'),
            array(
                'description' => __('Display a real-time clock for any city worldwide.', 'world-time-sync'),
                'classname' => 'wts-clock-widget',
            )
        );
    }

    public function widget($args, $instance) {
        $timezone = !empty($instance['timezone']) ? $instance['timezone'] : 'America/New_York';
        $theme = !empty($instance['theme']) ? $instance['theme'] : 'dark';
        $size = !empty($instance['size']) ? $instance['size'] : 'medium';
        $show_date = !empty($instance['show_date']) ? $instance['show_date'] : 'true';
        $title = !empty($instance['title']) ? $instance['title'] : '';

        echo $args['before_widget'];
        
        if (!empty($title)) {
            echo $args['before_title'] . esc_html($title) . $args['after_title'];
        }
        
        $clock = World_Time_Sync_Clock::get_instance();
        echo $clock->render_clock(array(
            'timezone' => $timezone,
            'theme' => $theme,
            'size' => $size,
            'show_date' => $show_date,
        ));
        
        echo $args['after_widget'];
    }

    public function form($instance) {
        $title = !empty($instance['title']) ? $instance['title'] : '';
        $timezone = !empty($instance['timezone']) ? $instance['timezone'] : 'America/New_York';
        $theme = !empty($instance['theme']) ? $instance['theme'] : 'dark';
        $size = !empty($instance['size']) ? $instance['size'] : 'medium';
        $show_date = !empty($instance['show_date']) ? $instance['show_date'] : 'true';
        
        $clock = World_Time_Sync_Clock::get_instance();
        ?>
        <p>
            <label for="<?php echo esc_attr($this->get_field_id('title')); ?>"><?php _e('Title (optional):', 'world-time-sync'); ?></label>
            <input class="widefat" id="<?php echo esc_attr($this->get_field_id('title')); ?>" 
                   name="<?php echo esc_attr($this->get_field_name('title')); ?>" 
                   type="text" value="<?php echo esc_attr($title); ?>">
        </p>
        <p>
            <label for="<?php echo esc_attr($this->get_field_id('timezone')); ?>"><?php _e('Timezone:', 'world-time-sync'); ?></label>
            <select class="widefat" id="<?php echo esc_attr($this->get_field_id('timezone')); ?>" 
                    name="<?php echo esc_attr($this->get_field_name('timezone')); ?>">
                <?php echo $clock->render_clock(array('timezone' => $timezone)); // Hack to get options ?>
            </select>
        </p>
        <?php
        // Proper timezone select
        $zones = array(
            'America/New_York' => 'New York', 'America/Chicago' => 'Chicago',
            'America/Denver' => 'Denver', 'America/Los_Angeles' => 'Los Angeles',
            'America/Toronto' => 'Toronto', 'America/Sao_Paulo' => 'São Paulo',
            'Europe/London' => 'London', 'Europe/Paris' => 'Paris',
            'Europe/Berlin' => 'Berlin', 'Europe/Madrid' => 'Madrid',
            'Europe/Moscow' => 'Moscow', 'Asia/Dubai' => 'Dubai',
            'Asia/Kolkata' => 'Mumbai', 'Asia/Singapore' => 'Singapore',
            'Asia/Shanghai' => 'Shanghai', 'Asia/Hong_Kong' => 'Hong Kong',
            'Asia/Tokyo' => 'Tokyo', 'Asia/Seoul' => 'Seoul',
            'Asia/Bangkok' => 'Bangkok', 'Australia/Sydney' => 'Sydney',
            'Pacific/Auckland' => 'Auckland', 'Pacific/Honolulu' => 'Honolulu',
            'Africa/Cairo' => 'Cairo', 'Africa/Johannesburg' => 'Johannesburg',
        );
        ?>
        <p>
            <label for="<?php echo esc_attr($this->get_field_id('timezone')); ?>"><?php _e('Timezone:', 'world-time-sync'); ?></label>
            <select class="widefat" id="<?php echo esc_attr($this->get_field_id('timezone')); ?>" 
                    name="<?php echo esc_attr($this->get_field_name('timezone')); ?>">
                <?php foreach ($zones as $tz => $label) : ?>
                    <option value="<?php echo esc_attr($tz); ?>" <?php selected($timezone, $tz); ?>>
                        <?php echo esc_html($label); ?>
                    </option>
                <?php endforeach; ?>
            </select>
        </p>
        <p>
            <label for="<?php echo esc_attr($this->get_field_id('theme')); ?>"><?php _e('Theme:', 'world-time-sync'); ?></label>
            <select class="widefat" id="<?php echo esc_attr($this->get_field_id('theme')); ?>" 
                    name="<?php echo esc_attr($this->get_field_name('theme')); ?>">
                <option value="dark" <?php selected($theme, 'dark'); ?>><?php _e('Dark', 'world-time-sync'); ?></option>
                <option value="light" <?php selected($theme, 'light'); ?>><?php _e('Light', 'world-time-sync'); ?></option>
            </select>
        </p>
        <p>
            <label for="<?php echo esc_attr($this->get_field_id('size')); ?>"><?php _e('Size:', 'world-time-sync'); ?></label>
            <select class="widefat" id="<?php echo esc_attr($this->get_field_id('size')); ?>" 
                    name="<?php echo esc_attr($this->get_field_name('size')); ?>">
                <option value="small" <?php selected($size, 'small'); ?>><?php _e('Small', 'world-time-sync'); ?></option>
                <option value="medium" <?php selected($size, 'medium'); ?>><?php _e('Medium', 'world-time-sync'); ?></option>
                <option value="large" <?php selected($size, 'large'); ?>><?php _e('Large', 'world-time-sync'); ?></option>
            </select>
        </p>
        <p>
            <label for="<?php echo esc_attr($this->get_field_id('show_date')); ?>"><?php _e('Show Date:', 'world-time-sync'); ?></label>
            <select class="widefat" id="<?php echo esc_attr($this->get_field_id('show_date')); ?>" 
                    name="<?php echo esc_attr($this->get_field_name('show_date')); ?>">
                <option value="true" <?php selected($show_date, 'true'); ?>><?php _e('Yes', 'world-time-sync'); ?></option>
                <option value="false" <?php selected($show_date, 'false'); ?>><?php _e('No', 'world-time-sync'); ?></option>
            </select>
        </p>
        <?php
    }

    public function update($new_instance, $old_instance) {
        $instance = array();
        $instance['title'] = sanitize_text_field($new_instance['title']);
        $instance['timezone'] = sanitize_text_field($new_instance['timezone']);
        $instance['theme'] = sanitize_text_field($new_instance['theme']);
        $instance['size'] = sanitize_text_field($new_instance['size']);
        $instance['show_date'] = sanitize_text_field($new_instance['show_date']);
        return $instance;
    }
}
