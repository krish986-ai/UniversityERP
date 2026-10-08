// Simple JavaScript for University ERP
// Handles basic UI interactions

document.addEventListener('DOMContentLoaded', function() {
    // Auto-hide flash messages after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            alert.style.transition = 'opacity 0.5s';
            alert.style.opacity = '0';
            setTimeout(function() {
                alert.remove();
            }, 500);
        }, 5000);
    });

    // Confirm delete actions
    const deleteButtons = document.querySelectorAll('.btn-delete');
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this record?')) {
                e.preventDefault();
            }
        });
    });

    // Auto-calculate due fee when paid fee changes
    const paidFeeInput = document.getElementById('paid_fee');
    const dueFeeInput = document.getElementById('due_fee');
    const totalFeeInput = document.getElementById('total_fee');
    const statusInput = document.getElementById('status');

    if (paidFeeInput && dueFeeInput && totalFeeInput) {
        paidFeeInput.addEventListener('input', function() {
            const total = parseInt(totalFeeInput.value) || 0;
            const paid = parseInt(paidFeeInput.value) || 0;
            const due = total - paid;
            dueFeeInput.value = due;
            
            if (statusInput) {
                statusInput.value = due <= 0 ? 'Paid' : 'Pending';
            }
        });
    }

    // Highlight current page in sidebar
    const currentPath = window.location.pathname;
    const sidebarLinks = document.querySelectorAll('.sidebar a');
    sidebarLinks.forEach(function(link) {
        if (link.getAttribute('href') === currentPath) {
            link.style.backgroundColor = '#2c3e50';
            link.style.color = 'white';
        }
    });

    // Form validation for marks input
    const marksInputs = document.querySelectorAll('.marks-input');
    marksInputs.forEach(function(input) {
        input.addEventListener('blur', function() {
            const value = parseInt(input.value);
            if (value < 0) input.value = 0;
            if (value > 100) input.value = 100;
        });
    });

    // Attendance select validation
    const attendanceSelects = document.querySelectorAll('.attendance-select');
    attendanceSelects.forEach(function(select) {
        select.addEventListener('change', function() {
            if (this.value === 'Present') {
                this.style.backgroundColor = '#e8f8f5';
            } else {
                this.style.backgroundColor = '#fdf2e9';
            }
        });
    });

    // Simple search/filter for tables (if needed)
    const searchInputs = document.querySelectorAll('input[data-search]');
    searchInputs.forEach(function(input) {
        const tableId = input.getAttribute('data-search');
        const table = document.getElementById(tableId);
        if (table) {
            input.addEventListener('input', function() {
                const filter = this.value.toLowerCase();
                const rows = table.querySelectorAll('tbody tr');
                rows.forEach(function(row) {
                    const text = row.textContent.toLowerCase();
                    row.style.display = text.includes(filter) ? '' : 'none';
                });
            });
        }
    });
});

// Utility functions
function formatCurrency(amount) {
    return new Intl.NumberFormat('en-IN', {
        style: 'currency',
        currency: 'INR',
        minimumFractionDigits: 0
    }).format(amount);
}

function calculatePercentage(present, total) {
    if (total === 0) return 0;
    return ((present / total) * 100).toFixed(1);
}

// Export for potential use in other scripts
window.UniversityERP = {
    formatCurrency,
    calculatePercentage
};