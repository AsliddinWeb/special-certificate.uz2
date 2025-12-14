// ================================
// SPECIAL CERTIFICATE - MAIN JS
// ================================

document.addEventListener('DOMContentLoaded', function() {

    // ============ Elements ============
    const navbar = document.getElementById('navbar');
    const topbar = document.querySelector('.topbar');
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const hamburgerIcon = document.querySelector('.hamburger-icon');
    const closeIcon = document.querySelector('.close-icon');
    const navLinks = document.querySelectorAll('.nav-link');
    const navText = document.querySelector('.nav-text');
    const backToTop = document.getElementById('back-to-top');
    const themeToggle = document.getElementById('theme-toggle');
    const mobileThemeToggle = document.getElementById('mobile-theme-toggle');

    // ============ Dark Mode ============
    function setTheme(theme) {
        if (theme === 'dark') {
            document.documentElement.classList.add('dark');
            localStorage.setItem('theme', 'dark');
        } else {
            document.documentElement.classList.remove('dark');
            localStorage.setItem('theme', 'light');
        }
    }

    function toggleTheme() {
        if (document.documentElement.classList.contains('dark')) {
            setTheme('light');
        } else {
            setTheme('dark');
        }
    }

    // Theme toggle buttons
    if (themeToggle) {
        themeToggle.addEventListener('click', toggleTheme);
    }

    if (mobileThemeToggle) {
        mobileThemeToggle.addEventListener('click', toggleTheme);
    }

    // ============ Navbar Scroll Effect ============
    function handleScroll() {
        if (!navbar) return;

        const scrollY = window.scrollY;
        const isDark = document.documentElement.classList.contains('dark');

        if (scrollY > 50) {
            // Navbar scrolled state
            navbar.classList.add('shadow-lg', 'top-0');
            navbar.classList.remove('md:top-[42px]');

            if (isDark) {
                navbar.classList.add('bg-gray-800');
                navbar.classList.remove('bg-white', 'bg-transparent');
            } else {
                navbar.classList.add('bg-white');
                navbar.classList.remove('bg-gray-800', 'bg-transparent');
            }

            // Hide topbar
            if (topbar) {
                topbar.classList.add('-translate-y-full');
            }

            // Change nav links colors
            navLinks.forEach(link => {
                link.classList.remove('text-white/90', 'hover:text-white');
                if (isDark) {
                    link.classList.add('text-gray-300', 'hover:text-white');
                } else {
                    link.classList.add('text-gray-700', 'hover:text-secondary');
                }
            });

            // Change logo text color
            if (navText) {
                navText.classList.remove('text-white');
                if (isDark) {
                    navText.classList.add('text-white');
                } else {
                    navText.classList.add('text-primary');
                }
            }

            // Change mobile button style
            if (mobileMenuBtn) {
                mobileMenuBtn.classList.remove('bg-white/10', 'border-white/20');
                if (isDark) {
                    mobileMenuBtn.classList.add('bg-gray-700', 'border-gray-600');
                } else {
                    mobileMenuBtn.classList.add('bg-gray-100', 'border-gray-200');
                }
            }
            if (hamburgerIcon) {
                hamburgerIcon.classList.remove('text-white');
                hamburgerIcon.classList.add(isDark ? 'text-white' : 'text-primary');
            }
            if (closeIcon) {
                closeIcon.classList.remove('text-white');
                closeIcon.classList.add(isDark ? 'text-white' : 'text-primary');
            }
        } else {
            // Navbar default state
            navbar.classList.remove('bg-white', 'bg-gray-800', 'shadow-lg', 'top-0');
            navbar.classList.add('bg-transparent', 'md:top-[42px]');

            // Show topbar
            if (topbar) {
                topbar.classList.remove('-translate-y-full');
            }

            // Reset nav links colors
            navLinks.forEach(link => {
                link.classList.add('text-white/90', 'hover:text-white');
                link.classList.remove('text-gray-700', 'hover:text-secondary', 'text-gray-300');
            });

            // Reset logo text color
            if (navText) {
                navText.classList.add('text-white');
                navText.classList.remove('text-primary');
            }

            // Reset mobile button style
            if (mobileMenuBtn) {
                mobileMenuBtn.classList.add('bg-white/10', 'border-white/20');
                mobileMenuBtn.classList.remove('bg-gray-100', 'border-gray-200', 'bg-gray-700', 'border-gray-600');
            }
            if (hamburgerIcon) {
                hamburgerIcon.classList.add('text-white');
                hamburgerIcon.classList.remove('text-primary');
            }
            if (closeIcon) {
                closeIcon.classList.add('text-white');
                closeIcon.classList.remove('text-primary');
            }
        }

        // Back to top button visibility
        if (backToTop) {
            if (scrollY > 500) {
                backToTop.classList.remove('opacity-0', 'invisible');
                backToTop.classList.add('opacity-100', 'visible');
            } else {
                backToTop.classList.remove('opacity-100', 'visible');
                backToTop.classList.add('opacity-0', 'invisible');
            }
        }
    }

    // Scroll event listener
    window.addEventListener('scroll', handleScroll);
    handleScroll(); // Initial check

    // ============ Mobile Menu Toggle ============
    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            mobileMenu.classList.toggle('hidden');

            if (hamburgerIcon && closeIcon) {
                hamburgerIcon.classList.toggle('hidden');
                closeIcon.classList.toggle('hidden');
            }
        });

        // Close menu when clicking on links
        const mobileLinks = mobileMenu.querySelectorAll('a');
        mobileLinks.forEach(link => {
            link.addEventListener('click', function() {
                mobileMenu.classList.add('hidden');
                if (hamburgerIcon && closeIcon) {
                    hamburgerIcon.classList.remove('hidden');
                    closeIcon.classList.add('hidden');
                }
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', function(e) {
            if (navbar && !navbar.contains(e.target) && !mobileMenu.classList.contains('hidden')) {
                mobileMenu.classList.add('hidden');
                if (hamburgerIcon && closeIcon) {
                    hamburgerIcon.classList.remove('hidden');
                    closeIcon.classList.add('hidden');
                }
            }
        });

        // Close menu on escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && !mobileMenu.classList.contains('hidden')) {
                mobileMenu.classList.add('hidden');
                if (hamburgerIcon && closeIcon) {
                    hamburgerIcon.classList.remove('hidden');
                    closeIcon.classList.add('hidden');
                }
            }
        });
    }

    // ============ Back to Top ============
    if (backToTop) {
        backToTop.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // ============ Smooth Scroll for Anchor Links ============
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');

            if (href !== '#' && href.length > 1) {
                const target = document.querySelector(href);

                if (target) {
                    e.preventDefault();
                    const offset = 100;
                    const position = target.getBoundingClientRect().top + window.pageYOffset - offset;

                    window.scrollTo({
                        top: position,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });

    // ============ Phone Input Formatting ============
    const phoneInput = document.querySelector('input[name="phone"]');

    if (phoneInput) {
        phoneInput.addEventListener('input', function(e) {
            let value = e.target.value.replace(/\D/g, '');

            if (value.length > 0 && !value.startsWith('998')) {
                value = '998' + value;
            }

            if (value.length > 12) {
                value = value.slice(0, 12);
            }

            let formatted = '';
            if (value.length > 0) formatted = '+' + value.slice(0, 3);
            if (value.length > 3) formatted += ' ' + value.slice(3, 5);
            if (value.length > 5) formatted += ' ' + value.slice(5, 8);
            if (value.length > 8) formatted += ' ' + value.slice(8, 10);
            if (value.length > 10) formatted += ' ' + value.slice(10, 12);

            e.target.value = formatted;
        });

        phoneInput.placeholder = '+998 90 123 45 67';
    }

    // ============ Form Submit Loading State ============
    const forms = document.querySelectorAll('form');

    forms.forEach(form => {
        form.addEventListener('submit', function() {
            const submitBtn = this.querySelector('button[type="submit"]');

            if (submitBtn && !submitBtn.disabled) {
                submitBtn.disabled = true;
                submitBtn.dataset.originalText = submitBtn.innerHTML;
                submitBtn.innerHTML = `
                    <svg class="animate-spin w-5 h-5 mr-2 inline" fill="none" viewBox="0 0 24 24">
                        <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                        <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                    </svg>
                    Yuborilmoqda...
                `;
            }
        });
    });

    // ============ Alert Auto Dismiss ============
    const alerts = document.querySelectorAll('[data-auto-dismiss]');

    alerts.forEach(alert => {
        const delay = parseInt(alert.getAttribute('data-auto-dismiss')) || 5000;

        setTimeout(() => {
            alert.style.transition = 'all 0.3s ease';
            alert.style.opacity = '0';
            alert.style.transform = 'translateY(-10px)';

            setTimeout(() => {
                alert.remove();
            }, 300);
        }, delay);
    });

    // ============ Language Selector ============
    const langButtons = document.querySelectorAll('[data-lang]');

    langButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            const lang = this.dataset.lang;

            // Update all language buttons
            document.querySelectorAll('[data-lang]').forEach(b => {
                if (b.dataset.lang === lang) {
                    b.classList.add('bg-secondary', 'text-white');
                    b.classList.remove('text-gray-400', 'hover:text-white', 'bg-gray-100', 'text-gray-600');
                } else {
                    b.classList.remove('bg-secondary', 'text-white');
                    // Check if it's in topbar or mobile menu
                    if (b.closest('.topbar')) {
                        b.classList.add('text-gray-400', 'hover:text-white');
                    } else {
                        b.classList.add('bg-gray-100', 'text-gray-600');
                    }
                }
            });

            localStorage.setItem('lang', lang);
            console.log('Language selected:', lang);
        });
    });

    // ============ External Links ============
    document.querySelectorAll('a[href^="http"]').forEach(link => {
        if (!link.href.includes(window.location.hostname)) {
            link.setAttribute('target', '_blank');
            link.setAttribute('rel', 'noopener noreferrer');
        }
    });

    // ============ Console Branding ============
    console.log(
        '%c Special Certificate ',
        'background: linear-gradient(135deg, #1E3A5F, #3B82F6); color: white; padding: 12px 24px; border-radius: 6px; font-size: 14px; font-weight: bold;'
    );

});

// ============ Utility Functions ============

function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

function throttle(func, limit) {
    let inThrottle;
    return function(...args) {
        if (!inThrottle) {
            func.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

function formatNumber(num) {
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
}

function getUrlParam(param) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(param);
}