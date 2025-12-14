/** @odoo-module **/

/**
 * Simstech Website Animations
 * Subtle motion cues for enhanced UX
 */

import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.SimstechAnimations = publicWidget.Widget.extend({
    selector: '.s_simstech_hero, .s_simstech_services, .s_simstech_problems, .s_simstech_work, .s_simstech_approach, .s_simstech_faq, .s_simstech_contact',
    
    start: function () {
        this._super.apply(this, arguments);
        this._setupAnimations();
        this._setupSmoothScroll();
        return Promise.resolve();
    },

    _setupAnimations: function () {
        // Intersection Observer for fade-in animations
        const observerOptions = {
            root: null,
            rootMargin: '0px',
            threshold: 0.1
        };

        const fadeObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('simstech-visible');
                    fadeObserver.unobserve(entry.target);
                }
            });
        }, observerOptions);

        // Observe all elements with fade-in class within this section
        this.$('.simstech-fade-in').each(function() {
            fadeObserver.observe(this);
        });
    },

    _setupSmoothScroll: function () {
        // Smooth scroll for anchor links within the section
        this.$('a[href^="#"]').on('click', function(e) {
            const targetId = $(this).attr('href');
            if (targetId === '#' || targetId === '#top') {
                e.preventDefault();
                window.scrollTo({ top: 0, behavior: 'smooth' });
                return;
            }
            
            const $target = $(targetId);
            if ($target.length) {
                e.preventDefault();
                const headerOffset = 80; // Account for sticky header
                const elementPosition = $target.offset().top;
                const offsetPosition = elementPosition - headerOffset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    },
});

export default publicWidget.registry.SimstechAnimations;
