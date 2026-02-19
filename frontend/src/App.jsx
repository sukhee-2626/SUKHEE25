import React, { useState, useEffect } from 'react';
import { Upload, Home, Info, AlertTriangle, CheckCircle2, Loader2, Compass } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import axios from 'axios';
import { Doughnut } from 'react-chartjs-2';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';

ChartJS.register(ArcElement, Tooltip, Legend);

const API_URL = 'http://localhost:5000';

function App() {
    const [image, setImage] = useState(null);
    const [preview, setPreview] = useState(null);
    const [loading, setLoading] = useState(false);
    const [results, setResults] = useState(null);
    const [error, setError] = useState(null);

    const handleImageChange = (e) => {
        const file = e.target.files[0];
        if (file) {
            setImage(file);
            setPreview(URL.createObjectURL(file));
            setResults(null);
            setError(null);
        }
    };

    const analyzeVastu = async () => {
        if (!image) return;

        setLoading(true);
        setError(null);

        const formData = new FormData();
        formData.append('image', image);

        try {
            const response = await axios.post(`${API_URL}/analyze`, formData, {
                headers: { 'Content-Type': 'multipart/form-data' },
            });
            setResults(response.data);
        } catch (err) {
            setError(err.response?.data?.error || 'Failed to connect to backend. Make sure the Flask server is running.');
        } finally {
            setLoading(false);
        }
    };

    const getScoreColor = (score) => {
        if (score > 80) return '#10B981'; // Green
        if (score > 50) return '#F59E0B'; // Amber
        return '#EF4444'; // Red
    };

    const chartData = results ? {
        datasets: [{
            data: [results.analysis.score, 100 - results.analysis.score],
            backgroundColor: [getScoreColor(results.analysis.score), '#1E293B'],
            borderWidth: 0,
            circumference: 180,
            rotation: 270,
        }],
    } : null;

    return (
        <div className="min-h-screen p-4 md:p-8 flex flex-col items-center bg-gradient-radial from-[#111827] to-[#05070A]">
            <header className="w-full max-w-6xl mb-12 flex flex-col items-center text-center">
                <motion.div
                    initial={{ opacity: 0, y: -20 }}
                    animate={{ opacity: 1, y: 0 }}
                    className="flex items-center gap-3 mb-4"
                >
                    <Compass className="w-10 h-10 text-orange-500 animate-pulse" />
                    <h1 className="text-4xl md:text-5xl font-bold gradient-text">VastuAI</h1>
                </motion.div>
                <p className="text-gray-400 max-w-2xl text-lg">
                    Transform your living space with AI-powered architectural analysis based on traditional Vastu Shastra principles.
                </p>
            </header>

            <main className="w-full max-w-6xl grid grid-cols-1 lg:grid-cols-2 gap-8 items-start">
                {/* Upload Section */}
                <motion.div
                    initial={{ opacity: 0, x: -30 }}
                    animate={{ opacity: 1, x: 0 }}
                    className="glass-card p-6 md:p-8 flex flex-col gap-6"
                >
                    <h2 className="text-2xl font-semibold flex items-center gap-2">
                        <Upload className="text-amber-400" /> Upload Floor Plan
                    </h2>

                    <div className="relative group">
                        <div className={`border-2 border-dashed rounded-2xl p-8 transition-all flex flex-col items-center justify-center gap-4 ${preview ? 'border-amber-500/50 bg-amber-500/5' : 'border-white/10 hover:border-white/30'}`}>
                            {preview ? (
                                <img src={preview} alt="Preview" className="max-h-[300px] rounded-xl shadow-lg border border-white/10" />
                            ) : (
                                <>
                                    <div className="w-16 h-16 rounded-full bg-white/5 flex items-center justify-center group-hover:bg-white/10 transition-colors">
                                        <Home className="w-8 h-8 text-gray-400" />
                                    </div>
                                    <div className="text-center">
                                        <p className="text-white font-medium">Click to upload or drag and drop</p>
                                        <p className="text-gray-500 text-sm mt-1">Supports JPG, PNG (Max 5MB)</p>
                                    </div>
                                </>
                            )}
                            <input
                                type="file"
                                accept="image/*"
                                onChange={handleImageChange}
                                className="absolute inset-0 opacity-0 cursor-pointer"
                            />
                        </div>
                    </div>

                    <button
                        onClick={analyzeVastu}
                        disabled={!image || loading}
                        className={`w-full py-4 rounded-2xl font-bold text-lg transition-all flex items-center justify-center gap-2 ${loading
                                ? 'bg-gray-800 text-gray-500 cursor-not-allowed'
                                : image
                                    ? 'bg-gradient-to-r from-orange-500 to-amber-600 hover:shadow-[0_0_30px_-5px_rgba(245,158,11,0.5)] active:scale-95'
                                    : 'bg-white/5 text-white/30 cursor-not-allowed'
                            }`}
                    >
                        {loading ? (
                            <>
                                <Loader2 className="animate-spin" /> Analyzing Architecture...
                            </>
                        ) : (
                            'Start Vastu Analysis'
                        )}
                    </button>

                    {error && (
                        <div className="bg-red-500/10 border border-red-500/20 text-red-400 p-4 rounded-xl flex items-center gap-3">
                            <AlertTriangle size={20} />
                            <p className="text-sm">{error}</p>
                        </div>
                    )}
                </motion.div>

                {/* Results Section */}
                <AnimatePresence mode="wait">
                    {results ? (
                        <motion.div
                            key="results"
                            initial={{ opacity: 0, x: 30 }}
                            animate={{ opacity: 1, x: 0 }}
                            exit={{ opacity: 0, x: 30 }}
                            className="flex flex-col gap-6"
                        >
                            {/* Score Card */}
                            <div className="glass-card p-6 flex flex-col items-center">
                                <h3 className="text-xl font-medium text-gray-300 mb-2">Vastu Compliance Score</h3>
                                <div className="relative w-64 h-32 flex items-center justify-center overflow-hidden">
                                    <Doughnut data={chartData} options={{ cutout: '85%', plugins: { legend: { display: false } } }} />
                                    <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 mt-4 text-center">
                                        <span className="text-5xl font-bold" style={{ color: getScoreColor(results.analysis.score) }}>
                                            {results.analysis.score}
                                        </span>
                                        <span className="text-gray-500 text-xl font-medium">/100</span>
                                    </div>
                                </div>
                            </div>

                            {/* Suggestions */}
                            <div className="glass-card p-6 flex flex-col gap-4">
                                <h3 className="text-xl font-semibold flex items-center gap-2">
                                    <Info className="text-blue-400" /> Key Insights & Corrections
                                </h3>
                                <div className="space-y-3 max-h-[300px] overflow-y-auto pr-2 custom-scrollbar">
                                    {results.analysis.suggestions.map((suggestion, idx) => (
                                        <div
                                            key={idx}
                                            className={`p-4 rounded-xl border ${suggestion.startsWith('✅') ? 'bg-green-500/5 border-green-500/10' : suggestion.startsWith('❌') ? 'bg-red-500/5 border-red-500/10' : 'bg-amber-500/5 border-amber-500/10'}`}
                                        >
                                            <p className="text-sm md:text-base leading-relaxed">{suggestion}</p>
                                        </div>
                                    ))}
                                </div>
                            </div>

                            {/* Explanation */}
                            <div className="glass-card p-6 bg-gradient-to-br from-indigo-500/10 to-purple-500/5 border-indigo-500/20">
                                <p className="italic text-gray-300 leading-relaxed text-center">
                                    "{results.analysis.explanation}"
                                </p>
                            </div>
                        </motion.div>
                    ) : !loading && (
                        <motion.div
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            className="h-full flex flex-col items-center justify-center text-center p-8 border-2 border-dashed border-white/5 rounded-3xl"
                        >
                            <div className="w-20 h-20 rounded-full bg-white/5 flex items-center justify-center mb-6">
                                <Compass className="w-10 h-10 text-gray-600" />
                            </div>
                            <h3 className="text-xl font-medium text-gray-400">Analysis Results will appear here</h3>
                            <p className="text-gray-600 mt-2 max-w-[300px]">Upload a floor plan and click analyze to see your Vastu score and detailed suggestions.</p>
                        </motion.div>
                    )}
                </AnimatePresence>
            </main>

            <footer className="mt-16 text-gray-500 text-sm pb-8">
                &copy; 2026 VastuAI • Powered by Gemini Vision AI
            </footer>
        </div>
    );
}

export default App;
