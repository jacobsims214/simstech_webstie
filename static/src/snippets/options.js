/** @odoo-module **/

/**
 * Simstech Snippet Editor Options
 * Custom options for the website editor
 */

import options from "@web_editor/js/editor/snippets/options";

// Hero section options
options.registry.SimstechHero = options.Class.extend({
    /**
     * @override
     */
    start: function () {
        return this._super.apply(this, arguments);
    },
});

export default {
    SimstechHero: options.registry.SimstechHero,
};
