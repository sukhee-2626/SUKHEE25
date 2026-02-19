const { useState, useEffect, useRef } = React;

function App() {
    const [preview, setPreview] = useState(null);
    const [loading, setLoading] = useState(false);
    const [results, setResults] = useState(null);
    const [error, setError] = useState(null);
    const [language, setLanguage] = useState('en'); // 'en' or 'ta'

    // UI Text Translations
    const uiText = {
        en: {
            title: "ELEVATE YOUR SPACE ENERGY",
            subtitle: "Unlock the ancient architectural wisdom of Vastu Shastra with modern AI Vision.",
            getStarted: "Get Started",
            learnMore: "Learn More",
            inputTitle: "Input Floor Plan",
            dropText: "Drop your blueprint here",
            analyzing: "ANALYZING GEOMETRY...",
            startBtn: "Start AI Analysis",
            scoreTitle: "Vastu Compliance Score",
            actionTitle: "Actionable Insights",
            awaiting: "Awaiting Blueprint",
            awaitingDesc: "Upload a floor plan to reveal the hidden energy matrix of your space using strict Vastu principles."
        },
        ta: {
            title: "உங்கள் இல்லத்தின் ஆற்றலை உயர்த்துங்கள்",
            subtitle: "நவீன AI தொழில்நுட்பத்துடன் பண்டைய வாஸ்து சாஸ்திரத்தின் ஞானத்தை பெறுங்கள்.",
            getStarted: "தொடங்கவும்",
            learnMore: "மேலும் அறிய",
            inputTitle: "வீட்டு வரைபடத்தை உள்ளிடவும்",
            dropText: "வரைபடத்தை இங்கே போடவும்",
            analyzing: "ஆராய்கிறது...",
            startBtn: "AI ஆய்வைத் தொடங்கவும்",
            scoreTitle: "வாஸ்து இணக்க மதிப்பெண்",
            actionTitle: "செயல்படுத்தக்கூடிய ஆலோசனைகள்",
            awaiting: "வரைபடத்திற்காக காத்திருக்கிறது",
            awaitingDesc: "உங்கள் இடத்தின் மறைந்திருக்கும் ஆற்றலை வெளிப்படுத்த வரைபடத்தைப் பதிவேற்றவும்."
        }
    };

    const t = uiText[language];

    const canvasRef = useRef(null);
    const chartRef = useRef(null);
    const fileRef = useRef(null);
    const resultsRef = useRef(null);

    const handleUpload = (e) => {
        const file = e.target.files[0];
        if (file) {
            setPreview(URL.createObjectURL(file));
            fileRef.current = file;
            setResults(null);
            setError(null);
        }
    };



    // --- PDF Download Function ---
    const downloadPDF = () => {
        const element = resultsRef.current;
        const opt = {
            margin: [10, 10, 10, 10], // top, right, bottom, left
            filename: `Vastu_Report_${new Date().toISOString().slice(0, 10)}.pdf`,
            image: { type: 'jpeg', quality: 0.98 },
            html2canvas: { scale: 2, useCORS: true, logging: true, letterRendering: true },
            jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' },
            pagebreak: { mode: ['avoid-all', 'css', 'legacy'] }
        };
        // Use html2pdf lib
        window.html2pdf().set(opt).from(element).save();
    };

    const analyzeVastu = async () => {
        if (!preview || !fileRef.current) return;

        setLoading(true);
        setError(null);

        const formData = new FormData();
        formData.append('image', fileRef.current);
        formData.append('language', language);

        try {
            const response = await fetch('/analyze', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || 'Analysis failed');
            }

            setResults(data);

            // Smooth scroll to results
            setTimeout(() => {
                resultsRef.current?.scrollIntoView({ behavior: 'smooth' });
            }, 100);

        } catch (err) {
            console.error("Backend Error:", err);
            setError(err.message === 'Failed to fetch' ? 'Connection Error: Backend not reachable.' : err.message);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        if (results && canvasRef.current) {
            if (chartRef.current) chartRef.current.destroy();
            const ctx = canvasRef.current.getContext('2d');

            // Chart Config
            chartRef.current = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: ['Score', 'Remaining'],
                    datasets: [{
                        data: [results.analysis.score, 100 - results.analysis.score],
                        backgroundColor: [
                            results.analysis.score > 80 ? '#10B981' : results.analysis.score > 50 ? '#F59E0B' : '#EF4444',
                            'rgba(255,255,255,0.05)'
                        ],
                        borderWidth: 0,
                        circumference: 240,
                        rotation: 240,
                        borderRadius: 20,
                    }]
                },
                options: {
                    cutout: '85%',
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { display: false }, tooltip: { enabled: false } },
                    animation: { animateScale: true, animateRotate: true }
                }
            });
        }
    }, [results]);

    return (
        <div className="min-h-screen p-6 md:p-12 flex flex-col items-center">
            {/* Navigation Bar (Desktop) */}
            <nav className="fixed top-0 left-0 w-full p-6 flex justify-between items-center z-50 bg-black/50 backdrop-blur-md border-b border-white/5">
                <div className="flex items-center gap-3">
                    <div className="w-10 h-10 bg-gradient-to-br from-orange-500 to-amber-600 rounded-lg flex items-center justify-center">
                        <i data-lucide="compass" className="text-white w-6 h-6"></i>
                    </div>
                    <span className="text-xl font-bold tracking-tight">Vastu<span className="text-amber-400">AI</span></span>
                </div>
                <div className="hidden md:flex gap-8 text-sm font-medium text-gray-400 items-center">
                    <a href="#" className="hover:text-white transition-colors">Analyzer</a>
                    <a href="#" className="hover:text-white transition-colors">Principles</a>
                    <a href="#" className="hover:text-white transition-colors">Premium</a>
                    <div className="lang-switch">
                        <div className={`lang-btn ${language === 'en' ? 'active' : ''}`} onClick={() => setLanguage('en')}>EN</div>
                        <div className={`lang-btn ${language === 'ta' ? 'active' : ''}`} onClick={() => setLanguage('ta')}>TA</div>
                    </div>
                </div>
                <button className="px-6 py-2 rounded-full border border-white/20 text-sm hover:bg-white/10 transition-colors">
                    Login
                </button>
            </nav>

            <header className="mt-24 mb-16 text-center animate-fade-in-down w-full max-w-4xl">
                <div className="flex flex-col items-center justify-center gap-6 mb-4 relative">
                    {/* Glowing background effect */}
                    <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[300px] bg-gradient-to-r from-orange-500/20 via-amber-500/10 to-transparent blur-[100px] rounded-full pointer-events-none float-slow"></div>

                    <div className="relative z-10 float-medium">
                        <h1 className="text-6xl md:text-8xl font-black gradient-text tracking-tighter leading-tight drop-shadow-2xl text-center">
                            {t.title}
                        </h1>
                    </div>
                </div>
                <p className="text-gray-400 text-lg md:text-2xl max-w-2xl mx-auto font-light tracking-wide leading-relaxed mt-4">
                    {t.subtitle}
                </p>
                <div className="flex justify-center gap-4 mt-8">
                    <button className="px-8 py-3 bg-white text-black font-bold rounded-full hover:scale-105 transition-transform">{t.getStarted}</button>
                    <button className="px-8 py-3 bg-white/10 border border-white/10 rounded-full hover:bg-white/20 transition-colors backdrop-blur-md">{t.learnMore}</button>
                </div>
            </header>

            <main className="w-full max-w-7xl grid grid-cols-1 lg:grid-cols-2 gap-12 items-start relative z-10">

                {/* Upload Section */}
                <section className="glass-card p-8 md:p-10 relative overflow-hidden group">
                    <div className="absolute top-0 right-0 w-64 h-64 bg-orange-500/10 rounded-full blur-3xl -translate-y-1/2 translate-x-1/2 pointer-events-none"></div>

                    <h2 className="text-2xl font-semibold mb-8 flex items-center gap-3 text-white/90">
                        <i data-lucide="scan-line" className="text-amber-400"></i>
                        {t.inputTitle}
                    </h2>

                    <div className={`scanner-container border-2 border-dashed border-white/10 rounded-3xl p-8 flex flex-col items-center justify-center min-h-[400px] bg-white/[0.02] hover:bg-white/[0.04] transition-all cursor-pointer relative overflow-hidden ${loading ? 'border-orange-500/30' : ''}`}>
                        {loading && <div className="scanner-line"></div>}

                        {preview ? (
                            <img src={preview} className={`max-h-[350px] rounded-xl shadow-2xl border border-white/10 transition-all duration-700 ${loading ? 'opacity-50 scale-95 blur-sm' : ''}`} />
                        ) : (
                            <div className="text-center group-hover:scale-105 transition-transform duration-300">
                                <div className="w-20 h-20 bg-white/5 rounded-full flex items-center justify-center mx-auto mb-6 border border-white/10 relative">
                                    <i data-lucide="upload-cloud" className="w-8 h-8 text-amber-400 relative z-10"></i>
                                    <div className="absolute inset-0 bg-amber-500/20 blur-xl rounded-full opacity-0 group-hover:opacity-100 transition-opacity"></div>
                                </div>
                                <p className="text-white font-medium text-lg">{t.dropText}</p>
                                <p className="text-gray-500 text-sm mt-2">Supports JPG, PNG • Max 10MB</p>
                            </div>
                        )}
                        <input type="file" className="absolute inset-0 opacity-0 cursor-pointer" onChange={handleUpload} disabled={loading} />

                        {loading && (
                            <div className="absolute inset-0 flex flex-col items-center justify-center z-20">
                                <span className="loader mb-4"></span>
                                <p className="text-amber-400 font-mono text-sm tracking-widest animate-pulse">{t.analyzing}</p>
                            </div>
                        )}
                    </div>

                    <button
                        onClick={analyzeVastu}
                        disabled={!preview || loading}
                        className={`w-full mt-8 py-5 rounded-2xl font-bold text-lg tracking-wide transition-all uppercase relative overflow-hidden group/btn ${preview && !loading
                            ? "bg-gradient-to-r from-orange-500 via-amber-500 to-orange-600 text-white shadow-[0_0_40px_-10px_rgba(245,158,11,0.5)] hover:shadow-[0_0_60px_-15px_rgba(245,158,11,0.7)] hover:scale-[1.02] cursor-pointer"
                            : "bg-white/5 text-gray-500 cursor-not-allowed border border-white/5"
                            }`}
                    >
                        <span className="relative z-10 flex items-center justify-center gap-2">
                            {loading ? "Processing..." : <>{t.startBtn} <i data-lucide="sparkles" className="w-5 h-5"></i></>}
                        </span>
                        {preview && !loading && <div className="absolute inset-0 bg-white/20 translate-y-full group-hover/btn:translate-y-0 transition-transform duration-300"></div>}
                    </button>

                    {error && (
                        <div className="mt-6 p-4 bg-red-500/10 border border-red-500/20 text-red-200 rounded-xl flex items-center gap-3 animate-pulse">
                            <i data-lucide="alert-triangle" className="w-5 h-5 text-red-500"></i>
                            <p className="text-sm font-medium">{error}</p>
                        </div>
                    )}
                </section>

                {/* Results Section */}
                <section ref={resultsRef} className="space-y-6">
                    {results ? (
                        <div className="space-y-6 animate-in fade-in slide-in-from-bottom-8 duration-700">


                            {/* Score Card */}
                            <div className="glass-card p-8 flex flex-col items-center text-center relative overflow-hidden pdf-break-avoid">
                                <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-transparent via-emerald-500 to-transparent opacity-50"></div>
                                <h3 className="text-gray-400 font-medium tracking-wider text-sm uppercase mb-6">{t.scoreTitle}</h3>
                                <div className="relative w-64 h-64 flex items-center justify-center">
                                    <canvas ref={canvasRef} className="z-10"></canvas>
                                    <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/4 text-center z-20">
                                        <span className={`text-6xl font-bold block ${results.analysis.score > 80 ? 'text-emerald-400' : results.analysis.score > 50 ? 'text-amber-400' : 'text-red-400'}`}>
                                            {results.analysis.score}
                                        </span>
                                        <span className="text-gray-600 text-xl font-medium">/100</span>
                                    </div>
                                    {/* Glow effect behind chart */}
                                    <div className={`absolute inset-0 blur-3xl opacity-20 rounded-full ${results.analysis.score > 80 ? 'bg-emerald-500' : 'bg-amber-500'}`}></div>
                                </div>
                            </div>

                            {/* Explanation Card */}
                            <div className="glass-card p-8 border-l-4 border-l-amber-500 bg-gradient-to-r from-amber-500/5 to-transparent pdf-break-avoid">
                                <div className="flex items-start gap-4">
                                    <i data-lucide="quote" className="text-amber-500 w-8 h-8 fill-current opacity-50"></i>
                                    <p className="text-lg text-gray-200 leading-relaxed italic">
                                        "{results.analysis.explanation}"
                                    </p>
                                </div>
                            </div>


                            {/* Suggestions */}
                            <div className="glass-card p-8">
                                <div className="flex justify-between items-center mb-6">
                                    <h3 className="text-xl font-semibold flex items-center gap-3 text-white">
                                        <i data-lucide="list-checks" className="text-blue-400"></i>
                                        {t.actionTitle}
                                    </h3>
                                    <button onClick={downloadPDF} className="px-4 py-2 text-sm bg-white/10 hover:bg-white/20 border border-white/20 rounded-lg transition-colors flex items-center gap-2">
                                        <i data-lucide="download" className="w-4 h-4"></i> Download PDF
                                    </button>
                                </div>
                                <div className="space-y-4 custom-scrollbar max-h-[600px] overflow-y-auto pr-2">

                                    {results.analysis.suggestions.map((s, i) => (
                                        <div
                                            key={i}
                                            className={`suggestion-item p-6 rounded-2xl border transition-all hover:translate-x-1 pdf-break-avoid ${s.suggestion_type === 'good'
                                                ? 'bg-emerald-500/5 border-emerald-500/20 hover:bg-emerald-500/10'
                                                : s.suggestion_type === 'defect'
                                                    ? 'bg-red-500/5 border-red-500/20 hover:bg-red-500/10'
                                                    : 'bg-amber-500/5 border-amber-500/20 hover:bg-amber-500/10'
                                                }`}
                                            style={{ animationDelay: `${i * 100}ms` }}
                                        >
                                            <div className="flex gap-4 items-start">
                                                <span className="text-2xl mt-1">
                                                    {s.suggestion_type === 'defect' ? '❌' : s.suggestion_type === 'good' ? '✅' : '⚠️'}
                                                </span>
                                                <div className="space-y-3 w-full">
                                                    <h4 className="text-lg font-semibold text-white/90 leading-tight">
                                                        {s.card_title}
                                                    </h4>

                                                    {s.impact && (
                                                        <div className="grid grid-cols-[80px_1fr] gap-2 text-sm">
                                                            <span className="text-red-300 font-medium uppercase tracking-wider text-xs pt-1">Impact</span>
                                                            <p className="text-gray-300 calling-tighter">{s.impact}</p>
                                                        </div>
                                                    )}

                                                    {s.remedy && (
                                                        <div className="grid grid-cols-[80px_1fr] gap-2 text-sm bg-white/5 p-3 rounded-lg border border-white/5">
                                                            <span className="text-emerald-300 font-medium uppercase tracking-wider text-xs pt-1">Remedy</span>
                                                            <p className="text-gray-200">{s.remedy}</p>
                                                        </div>
                                                    )}

                                                    {s.detail && (
                                                        <div className="grid grid-cols-[80px_1fr] gap-2 text-sm bg-blue-500/5 p-3 rounded-lg border border-blue-500/10">
                                                            <span className="text-blue-300 font-medium uppercase tracking-wider text-xs pt-1">Detail</span>
                                                            <p className="text-gray-200 leading-relaxed text-xs opacity-80">{s.detail}</p>
                                                        </div>
                                                    )}
                                                </div>
                                            </div>
                                        </div>
                                    ))}
                                </div>
                            </div>
                        </div>
                    ) : (
                        <div className="glass-card p-12 h-full min-h-[500px] flex flex-col items-center justify-center text-center opacity-40 border-dashed border-2 border-white/5 bg-gradient-to-br from-white/[0.02] to-transparent">
                            <div className="w-32 h-32 rounded-full bg-white/5 flex items-center justify-center mb-8 animate-pulse relative">
                                <div className="absolute inset-0 border border-white/10 rounded-full animate-ping opacity-20"></div>
                                <i data-lucide="layers" className="w-12 h-12 text-gray-500"></i>
                            </div>
                            <h3 className="text-3xl font-medium text-gray-300 mb-4">{t.awaiting}</h3>
                            <p className="text-gray-500 text-lg max-w-sm leading-relaxed">
                                {t.awaitingDesc}
                            </p>
                        </div>
                    )}

                    {/* PDF Footer Report Credit - Visible in Download */}
                    {results && (
                        <div className="text-center pt-12 pb-4 border-t border-white/5 mt-8 pdf-break-avoid opacity-70">
                            <p className="text-gray-500 text-xs uppercase tracking-widest">Report Generated by VastuAI</p>
                            <p className="text-amber-500/80 font-medium text-sm mt-1">Done by: Sukhee Sakthivel GM</p>
                        </div>
                    )}
                </section>
            </main>

            {/* Footer */}
            <footer className="mt-24 py-8 text-center text-gray-600 text-sm relative z-10 w-full border-t border-white/5 bg-black/40 backdrop-blur-md">
                <div className="flex flex-col items-center gap-2">
                    <p>&copy; 2024 VastuAI. All rights reserved.</p>
                    <p className="text-amber-500/80 font-medium tracking-wide flex items-center gap-2">
                        <span className="w-1 h-1 rounded-full bg-amber-500"></span>
                        Done by: Sukhee Sakthivel GM
                        <span className="w-1 h-1 rounded-full bg-amber-500"></span>
                    </p>
                </div>
            </footer>
        </div >
    );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);

// Initialize particles with a darker, more premium config
particlesJS("particles-js", {
    "particles": {
        "number": { "value": 80, "density": { "enable": true, "value_area": 800 } },
        "color": { "value": ["#FFD700", "#FF8C00", "#ffffff"] },
        "shape": { "type": "circle" },
        "opacity": { "value": 0.3, "random": true, "anim": { "enable": true, "speed": 1, "opacity_min": 0.1, "sync": false } },
        "size": { "value": 3, "random": true, "anim": { "enable": true, "speed": 2, "size_min": 0.1, "sync": false } },
        "line_linked": { "enable": true, "distance": 150, "color": "#ffffff", "opacity": 0.05, "width": 1 },
        "move": { "enable": true, "speed": 1.5, "direction": "none", "random": true, "straight": false, "out_mode": "out", "bounce": false, "attract": { "enable": false, "rotateX": 600, "rotateY": 1200 } }
    },
    "interactivity": {
        "detect_on": "window",
        "events": { "onhover": { "enable": true, "mode": "repulse" }, "onclick": { "enable": true, "mode": "push" }, "resize": true },
        "modes": { "repulse": { "distance": 100, "duration": 0.4 }, "push": { "particles_nb": 4 } }
    },
    "retina_detect": true
});

// Initialize Icons
setTimeout(() => lucide.createIcons(), 500);
