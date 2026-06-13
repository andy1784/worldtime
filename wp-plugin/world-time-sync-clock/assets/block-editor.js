(function(wp) {
    var registerBlockType = wp.blocks.registerBlockType;
    var InspectorControls = wp.blockEditor.InspectorControls;
    var PanelBody = wp.components.PanelBody;
    var SelectControl = wp.components.SelectControl;
    var TextControl = wp.components.TextControl;
    var ServerSideRender = wp.serverSideRender;
    var __ = wp.i18n.__;
    
    var timezoneOptions = wtsBlockData.timezoneOptions || [];
    var defaultTimezone = wtsBlockData.defaultTimezone || 'America/New_York';
    var defaultTheme = wtsBlockData.defaultTheme || 'dark';
    var defaultSize = wtsBlockData.defaultSize || 'medium';
    
    registerBlockType('world-time-sync/clock', {
        title: __('World Time Clock', 'world-time-sync'),
        icon: 'clock',
        category: 'widgets',
        description: __('Display a real-time clock for any city worldwide.', 'world-time-sync'),
        
        attributes: {
            timezone: {
                type: 'string',
                default: defaultTimezone,
            },
            theme: {
                type: 'string',
                default: defaultTheme,
            },
            size: {
                type: 'string',
                default: defaultSize,
            },
            showDate: {
                type: 'string',
                default: 'true',
            },
        },
        
        edit: function(props) {
            var attributes = props.attributes;
            var setAttributes = props.setAttributes;
            
            return wp.element.createElement('div', { className: props.className },
                wp.element.createElement(InspectorControls, null,
                    wp.element.createElement(PanelBody, { title: __('Clock Settings', 'world-time-sync'), initialOpen: true },
                        wp.element.createElement(SelectControl, {
                            label: __('Timezone', 'world-time-sync'),
                            value: attributes.timezone,
                            options: timezoneOptions,
                            onChange: function(val) { setAttributes({ timezone: val }); },
                        }),
                        wp.element.createElement(SelectControl, {
                            label: __('Theme', 'world-time-sync'),
                            value: attributes.theme,
                            options: [
                                { value: 'dark', label: __('Dark', 'world-time-sync') },
                                { value: 'light', label: __('Light', 'world-time-sync') },
                            ],
                            onChange: function(val) { setAttributes({ theme: val }); },
                        }),
                        wp.element.createElement(SelectControl, {
                            label: __('Size', 'world-time-sync'),
                            value: attributes.size,
                            options: [
                                { value: 'small', label: __('Small (220×120)', 'world-time-sync') },
                                { value: 'medium', label: __('Medium (300×160)', 'world-time-sync') },
                                { value: 'large', label: __('Large (420×220)', 'world-time-sync') },
                            ],
                            onChange: function(val) { setAttributes({ size: val }); },
                        }),
                        wp.element.createElement(SelectControl, {
                            label: __('Show Date', 'world-time-sync'),
                            value: attributes.showDate,
                            options: [
                                { value: 'true', label: __('Yes', 'world-time-sync') },
                                { value: 'false', label: __('No', 'world-time-sync') },
                            ],
                            onChange: function(val) { setAttributes({ showDate: val }); },
                        })
                    )
                ),
                wp.element.createElement('div', { 
                    style: {
                        background: '#1a1a2e',
                        borderRadius: '12px',
                        padding: '20px',
                        textAlign: 'center',
                        color: '#fff',
                        border: '1px dashed rgba(255,255,255,0.2)'
                    }
                },
                    wp.element.createElement('div', { style: { fontSize: '12px', opacity: 0.5, marginBottom: 8 } },
                        '🕐 World Time Clock'
                    ),
                    wp.element.createElement('div', { style: { fontSize: '24px', fontWeight: 700, fontFamily: 'monospace' } },
                        '--:--:--'
                    ),
                    wp.element.createElement('div', { style: { fontSize: 11, opacity: 0.4, marginTop: 4 } },
                        timezoneOptions.find(function(o) { return o.value === attributes.timezone; })?.label || attributes.timezone
                    ),
                    wp.element.createElement('div', { style: { fontSize: 10, opacity: 0.3, marginTop: 8 } },
                        attributes.theme + ' · ' + attributes.size + ' · ' + (attributes.showDate === 'true' ? 'with date' : 'no date')
                    )
                )
            );
        },
        
        save: function() {
            // Dynamic block - rendered on server
            return null;
        },
    });
})(window.wp);
