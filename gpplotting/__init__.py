import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import warnings 
from scipy.stats import pearsonr, gaussian_kde

warnings.filterwarnings('ignore')

def example_plot():
    df = sns.load_dataset("iris")
    sns.pairplot(df, hue="species")

# For use with ridgeplot
# Define and use a simple function to label the kde plots in axes coordinates
def label(x, color, label, text_xpos, text_ypos, text_ha, text_va):
    ax = plt.gca()
    ax.text(text_xpos, text_ypos, label, color=color,
            ha=text_ha, va=text_va, transform=ax.transAxes)

'''
Creates a ridgeplot of overlapping kde plots

##########
PARAMETERS
    df : DataFrame
    x, hue : strings
        Variables that define subsets of the data to plot on the FacetGrid. x defines the variable that
        will be plotted on the x-axis; hue defines the variable that will be plotted on the rows.
    aspect : scalar, optional
        Defines aspect ratio of FacetGrid
    height : scalar, optional
        Defines height of each row in FacetGrid
    alpha : scalar, optional
        Defines opacity of kde plot
    text_xpos, text_ypos : scalar, optional
        Specify the horizontal and vertical positions of text labels
    text_ha, text_va : strings, optional
        Specify the horizontal and vertical alignments of text labels 
    lw : scalar, optional
        Specifies the linewidth for kdeplot
    kwargs : key, value pairings
        Other keyword arguments are passed through to the FacetGrid

This code is slightly modified from https://seaborn.pydata.org/examples/kde_ridgeplot
'''

def ridgeplot(df, x, hue, aspect=5, height=1, alpha=0.7, text_xpos=0, text_ypos=0.2, text_ha='left', 
              text_va='center', lw=0.5, **kwargs):
    
    # Change background to be transparent and set style to white
    sns.set(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})
    
    # Initialize a facetgrid
    g = sns.FacetGrid(df, row=hue, hue=hue, aspect=aspect, height=height, **kwargs)

    # Draw the densities in a few steps
    g.map(sns.kdeplot, x, clip_on=False, shade=True, alpha=alpha, lw=lw)

    # Label axes with the values from hue
    g.map(label, x, text_xpos=text_xpos, text_ypos=text_ypos, text_ha=text_ha, text_va=text_va)

    # Set the subplots to overlap
    g.fig.subplots_adjust(hspace=-0.25)

    # Remove axes details that don't play well with overlap
    g.set_titles('')
    g.set(yticks=[])
    g.despine(bottom=True, left=True)
    return g

'''
Creates a rasterized density plot

##########
PARAMETERS
    df : DataFrame with values to plot
    col1: Column name of the values for the x-axis
    col2: Column name of the values for the y-axis

'''
def gen_density_plot(df, col1, col2, cmap):
    x = np.array(df.ix[:, col1])
    y = np.array(df.ix[:, col2])
    corr = np.round(pearsonr(x, y)[0],2)
    xy = np.vstack([x,y])
    z = gaussian_kde(xy)(xy)
    idx = z.argsort()
    x, y, z = x[idx], y[idx], z[idx]
    fig, ax = plt.subplots()
    den = ax.scatter(x, y, c=z, s=50, edgecolor='', cmap=cmap, rasterized=True)
    cbar = fig.colorbar(den)
    cbar.solids.set_edgecolor("face")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.xaxis.set_tick_params(bottom='on', top='off')
    ax.yaxis.set_tick_params(left='on', right='off')
    ax.set_xlabel(col1)
    ax.set_ylabel(col2)
    ax.text(np.min(ax.get_xlim())+1,np.max(ax.get_ylim())-0.5,'r = '+str(corr))
    return