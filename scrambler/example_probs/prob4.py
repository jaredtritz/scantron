question_tex = r"""
%Question
\section{Here is an example problem...}
Here is the text of the problem.

\begin{equation}
    \label{simple_equation}
    \alpha = \sqrt{ \beta }
\end{equation}
"""

solution_tex = r"""
\textbf{Solution:} In principle, you could solve this problem by writing out two loop equations and one junction equation, and then solving the three equations simultaneously for three unknowns.  It is likely that this will be tedious and error prone.  It pays off to think strategically ahead of time.  Ask yourself: is it possible to tackle one unknown at a time?
   
I have marked the two junctions in the diagram as point \textbf{a} and point \textbf{b}.  The voltage difference between these two points \textbf{must} be the same regardless of the path that you take between them.

\begin{minipage}{0.8\linewidth}
\begin{center}
\includegraphics[height=2.3in]{example.jpg}
\end{center}
\end{minipage}

We know both the current and the resistance on the path between \textbf{a} and \textbf{b} that goes through the 40~Volt battery, so we can use that path to find the voltage:
$$
V_{\rm ab} = V_a - V_b = 40~{\rm Volts} - (2.0~{\rm Amps})\cdot(14~\Omega) = 12~{\rm Volts}
$$

Now that we have this voltage we can use it to find the current through the 60~$\Omega$ resistor:
$$
V_{\rm ab} = I_{60} (60~\Omega) \rightarrow I_{60} = 0.2~{\rm Amps}
$$

With both the current through the 40~Volt battery and the current through the 60~$\Omega$ resistor in hand we have enough information to easily apply the junction rule to get the current through the resistor $R$.  Either of the junctions will give the same result:
$$
I = I_{60} + I_{\rm R} \rightarrow I_{\rm R} = 1.8~{\rm Amps}
$$

The voltage along the path that includes resistor $R$ must still be 12~Volts, so we can now solve for $R$:
$$
V_{\rm ab} = I_{\rm R} R - 12~{\rm Volts} \rightarrow R = 13.3~\Omega
$$
"""

answers = [
r"""$R=13~\Omega$ (correct answer)""",
r"""$R=26~\Omega$""",
r"""$R=42~\Omega$""",
r"""$R=5.3~\Omega$""",
r"""$R=19~\Omega$"""
]


